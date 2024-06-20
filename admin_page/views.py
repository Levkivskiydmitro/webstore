import flask
from registration_page.models import User
from shop_page.models import Product
from project.settings import db
import os

def render_admin():

    if flask.request.method == 'POST':
        try:

            if flask.request.form.get('submit-change') != None:
                #

                list_values = flask.request.form.get('submit-change').split('-')
                
                product_name = Product.query.get(int(list_values[1]))
                
                #
                
                if list_values[0] == 'image':
                    # os.remove(os.path.abspath(__file__ + f"/../../static/shop_page/img\\{product_name.name}.png"))
                
                    image_save = flask.request.files['image']
                
                    image_save.save(os.path.abspath(__file__ + f"/../../static/shop_page/img/{product_name.name}.png"))
                
                #    
                
                elif list_values[0] == 'name':
                    get_name = flask.request.form.get('name')
                    
                    absolute_path = os.path.abspath(__file__ + f"/../../static/shop_page/img/")

                    # os.rename(src= absolute_path + f'/{product_name.name}.png', dst= absolute_path + f'//{get_name}.png')
                    
                    product_name.name = get_name
                    
                    db.session.commit()
            pass
        except Exception as e:
            print(f"{e}")

    
    return flask.render_template(template_name_or_list='admin.html', login = User.query.all(), products = Product.query.all())