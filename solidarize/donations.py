from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from datetime import datetime
from .extensions import db
from .models import Donation, Donor, Campaign

donations_bp = Blueprint("donations", __name__)

@donations_bp.route("/")
@login_required
def list():
    donations = Donation.query.order_by(Donation.date.desc()).all()
    donors = Donor.query.all()
    campaigns = Campaign.query.all()
    return render_template("donations/list.html", donations=donations, donors=donors, campaigns=campaigns)

@donations_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    donors = Donor.query.all()
    campaigns = Campaign.query.all()
    if request.method == "POST":
        donor_id = int(request.form.get("donor_id"))
        campaign_id = int(request.form.get("campaign_id"))
        amount = float(request.form.get("amount") or 0)
        date_str = request.form.get("date")
        note = request.form.get("note", "").strip()
        date = datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else datetime.utcnow().date()
        if amount <= 0:
            flash("Valor deve ser maior que zero.", "warning")
            return render_template("donations/form.html", donors=donors, campaigns=campaigns)
        d = Donation(donor_id=donor_id, campaign_id=campaign_id, amount=amount, date=date, note=note)
        db.session.add(d)
        db.session.commit()
        flash("Doação registrada.", "success")
        return redirect(url_for("donations.list"))
    return render_template("donations/form.html", donors=donors, campaigns=campaigns)

@donations_bp.route("/<int:id>/delete", methods=["POST"])
@login_required
def delete(id):
    d = Donation.query.get_or_404(id)
    db.session.delete(d)
    db.session.commit()
    flash("Doação removida.", "info")
    return redirect(url_for("donations.list"))
