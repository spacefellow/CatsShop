from models import *

app = create_app()


def add_admin():
    admin.add_view(ModelView(Cat, db.session))


@app.route('/', methods=["GET", "POST"])
def router():
    text = request.args.get('text')
    if text:
        return redirect(url_for('search', **request.args))
    return redirect(url_for('all_posts', **request.args))


@app.route('/cats', methods=["GET", "POST"], defaults={"page": 1})
@app.route('/cats/<int:page>', methods=["GET", "POST"])
def all_posts(page):
    if request.args.get('sort_by_breed'):
        cats = Cat.query.order_by(Cat.breed).paginate(page=page, per_page=per_page)
    elif request.args.get('sort_by_age'):
        if request.args.get('desc'):
            cats = Cat.query.order_by(Cat.age.desc()).paginate(page=page, per_page=per_page)
        else:
            cats = Cat.query.order_by(Cat.age).paginate(page=page, per_page=per_page)
    else:
        cats = Cat.query.paginate(page=page, per_page=per_page)
    return render_template('cats.html', cats=cats)


@app.route('/cat/<int:id>', methods=["GET", "POST"])
def post_detail(id):
    cat = Cat.query.get_or_404(id)
    return render_template("cat_detail.html", cat=cat)


@app.route('/search', methods=["GET", "POST"], defaults={"page": 1})
@app.route('/search/<int:page>', methods=["GET", "POST"])
def search(page):
    keyword = request.args.get('text').lower()
    cats = Cat.query.filter(or_(keyword == func.lower(Cat.name),
                                keyword == Cat.age.cast(String),
                                func.lower(Cat.breed).contains(keyword),
                                func.lower(Cat.info).contains(keyword))).paginate(page=page, per_page=per_page)
    return render_template("cats.html", cats=cats, title='Поиск' + keyword)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')
