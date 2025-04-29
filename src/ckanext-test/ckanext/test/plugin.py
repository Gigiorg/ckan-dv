import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.plugins.interfaces import IBlueprint
from flask import Blueprint, render_template, request
import os
import requests
import json


# import ckanext.test.cli as cli
# import ckanext.test.helpers as helpers
# import ckanext.test.views as views
# from ckanext.test.logic import (
#     action, auth, validators
# )


class TestPlugin(plugins.SingletonPlugin):
    plugins.implements(IBlueprint)
    plugins.implements(plugins.IConfigurer)
    
    # plugins.implements(plugins.IAuthFunctions)
    # plugins.implements(plugins.IActions)
    # plugins.implements(plugins.IBlueprint)
    # plugins.implements(plugins.IClick)
    # plugins.implements(plugins.ITemplateHelpers)
    # plugins.implements(plugins.IValidators)
    

    def get_blueprint(self):
        test_bp = Blueprint('test_plugin', __name__, url_prefix='')

        @test_bp.route('/')
        def home():
            api_token = 'b50f1991-d20f-4ed3-b071-5f301f86a265'
            server_url = 'http://192.168.220.58:8080'
            dataset_id = 'root'

            url = f"{server_url}/api/dataverses/{dataset_id}/contents"
            headers = {"X-Dataverse-key": api_token}
            
        
            try:
                #response = requests.get(url, headers=headers)
                response = requests.get(url)
                data = response.json() if response.status_code == 200 else {"error": "Failed to fetch data"}
            except Exception as e:
                data = {"error": str(e)}

            return render_template('home.html', data=json.dumps(data, indent=2))

        return test_bp
    
    def update_config(self, config_):
        # Register template directory
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public") 
        toolkit.add_resource("assets", "test")    
    # IAuthFunctions

    # def get_auth_functions(self):
    #     return auth.get_auth_functions()

    # IActions

    # def get_actions(self):
    #     return action.get_actions()

    # IBlueprint

    # def get_blueprint(self):
    #     return views.get_blueprints()

    # IClick

    # def get_commands(self):
    #     return cli.get_commands()

    # ITemplateHelpers

    # def get_helpers(self):
    #     return helpers.get_helpers()

    # IValidators

    # def get_validators(self):
    #     return validators.get_validators()
    
