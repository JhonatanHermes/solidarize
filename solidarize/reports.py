from flask import Blueprint, send_file, request, flash, redirect, url_for
from flask_login import login_required
from io import BytesIO
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib import colors
from .extensions import db
from .models import Donation, Campaign

reports_bp = Blueprint("reports", __name__)

@reports_bp.route("/monthly")
@login_required
def monthly():
    # Params: ?year=2025&month=10
    now = datetime.utcnow()
    year = int(request.args.get("year", now.year))
    month = int(request.args.get("month", now.month))
    start = datetime(year, month, 1)
    if month == 12:
        end = datetime(year+1, 1, 1)
    else:
        end = datetime(year, month+1, 1)

    donations = Donation.query.filter(Donation.date >= start, Donation.date < end).all()
    total = sum(d.amount for d in donations)

    # Generate PDF
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Header
    p.setFillColor(colors.HexColor("#333333"))
    p.setFont("Helvetica-Bold", 16)
    p.drawString(2*cm, height - 2*cm, f"Relatório Mensal de Doações - {month:02d}/{year}")
    p.setFont("Helvetica", 10)
    p.setFillColor(colors.black)
    p.drawString(2*cm, height - 2.7*cm, f"Total arrecadado: R$ {total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

    # Table header
    y = height - 3.5*cm
    p.setFont("Helvetica-Bold", 10)
    p.drawString(2*cm, y, "Data")
    p.drawString(5*cm, y, "Campanha")
    p.drawString(12*cm, y, "Valor (R$)")
    y -= 0.5*cm
    p.setFont("Helvetica", 10)

    for d in donations:
        campaign = Campaign.query.get(d.campaign_id)
        p.drawString(2*cm, y, d.date.strftime("%d/%m/%Y"))
        p.drawString(5*cm, y, (campaign.title if campaign else "-")[:40])
        p.drawRightString(15*cm, y, f"{d.amount:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        y -= 0.5*cm
        if y < 2*cm:
            p.showPage()
            y = height - 2*cm

    p.showPage()
    p.save()
    buffer.seek(0)
    filename = f"relatorio_{year}_{month:02d}.pdf"
    return send_file(buffer, as_attachment=True, download_name=filename, mimetype="application/pdf")
