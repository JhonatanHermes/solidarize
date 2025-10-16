from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Donation
from .extensions import db

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
@login_required
def index():
    total = db.session.query(db.func.sum(Donation.amount)).scalar() or 0.0
    count = db.session.query(Donation).count()
    return render_template("index.html", total=total, count=count)
