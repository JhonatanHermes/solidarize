from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from .extensions import db
from .models import Donor

donors_bp = Blueprint("donors", __name__)

@donors_bp.route("/")
@login_required
def list():
    q = request.args.get("q", "").strip()
    query = Donor.query
    if q:
        query = query.filter(Donor.name.ilike(f"%{q}%"))
    donors = query.order_by(Donor.created_at.desc()).all()
    return render_template("donors/list.html", donors=donors, q=q)

@donors_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        if not name:
            flash("Nome é obrigatório.", "warning")
            return render_template("donors/form.html")
        donor = Donor(name=name, email=email, phone=phone)
        db.session.add(donor)
        db.session.commit()
        flash("Doador cadastrado.", "success")
        return redirect(url_for("donors.list"))
    return render_template("donors/form.html")

@donors_bp.route("/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit(id):
    donor = Donor.query.get_or_404(id)
    if request.method == "POST":
        donor.name = request.form.get("name", "").strip()
        donor.email = request.form.get("email", "").strip()
        donor.phone = request.form.get("phone", "").strip()
        db.session.commit()
        flash("Dados atualizados.", "success")
        return redirect(url_for("donors.list"))
    return render_template("donors/form.html", donor=donor)

@donors_bp.route("/<int:id>/delete", methods=["POST"])
@login_required
def delete(id):
    donor = Donor.query.get_or_404(id)
    db.session.delete(donor)
    db.session.commit()
    flash("Doador removido.", "info")
    return redirect(url_for("donors.list"))
