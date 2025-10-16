from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from datetime import datetime
from .extensions import db
from .models import Campaign

campaigns_bp = Blueprint("campaigns", __name__)

@campaigns_bp.route("/")
@login_required
def list():
    campaigns = Campaign.query.order_by(Campaign.created_at.desc()).all()
    return render_template("campaigns/list.html", campaigns=campaigns)

@campaigns_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        goal = float(request.form.get("goal", "0") or 0)
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        sd = datetime.strptime(start_date, "%Y-%m-%d").date() if start_date else None
        ed = datetime.strptime(end_date, "%Y-%m-%d").date() if end_date else None
        if not title:
            flash("Título é obrigatório.", "warning")
            return render_template("campaigns/form.html")
        c = Campaign(title=title, description=description, goal=goal, start_date=sd, end_date=ed)
        db.session.add(c)
        db.session.commit()
        flash("Campanha criada.", "success")
        return redirect(url_for("campaigns.list"))
    return render_template("campaigns/form.html")

@campaigns_bp.route("/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit(id):
    c = Campaign.query.get_or_404(id)
    if request.method == "POST":
        c.title = request.form.get("title", "").strip()
        c.description = request.form.get("description", "").strip()
        c.goal = float(request.form.get("goal", "0") or 0)
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        from datetime import datetime
        c.start_date = datetime.strptime(start_date, "%Y-%m-%d").date() if start_date else None
        c.end_date = datetime.strptime(end_date, "%Y-%m-%d").date() if end_date else None
        db.session.commit()
        flash("Campanha atualizada.", "success")
        return redirect(url_for("campaigns.list"))
    return render_template("campaigns/form.html", campaign=c)

@campaigns_bp.route("/<int:id>/delete", methods=["POST"])
@login_required
def delete(id):
    c = Campaign.query.get_or_404(id)
    db.session.delete(c)
    db.session.commit()
    flash("Campanha removida.", "info")
    return redirect(url_for("campaigns.list"))
