from ckan.plugins import implements, SingletonPlugin
from ckan.plugins.interfaces import IBlueprint, IConfigurer
from flask import Blueprint, render_template, request
import ckan.plugins.toolkit as toolkit
import os
import requests
import json
import logging

log = logging.getLogger(__name__)


# import ckanext.test.cli as cli
# import ckanext.test.helpers as helpers
# import ckanext.test.views as views
# from ckanext.test.logic import (
#     action, auth, validators
# )


class TestPlugin(SingletonPlugin):
    implements(IBlueprint)
    implements(IConfigurer)
    #implements(IBootstrap)

    
    # plugins.implements(plugins.IAuthFunctions)
    # plugins.implements(plugins.IActions)
    # plugins.implements(plugins.IBlueprint)
    # plugins.implements(plugins.IClick)
    # plugins.implements(plugins.ITemplateHelpers)
    # plugins.implements(plugins.IValidators)
    

    def get_blueprint(self):
        test_bp = Blueprint('test_plugin', __name__, url_prefix='')

        @test_bp.route('/my_template.html')
        def custom_route():
            api_token = '14350175-e540-46db-979f-62916e8c4185'
            server_url = 'http://192.168.220.68:8080'
            dataset_id = 'REDGEN_GNSS_ATIC'

            url = f"{server_url}/api/dataverses/{dataset_id}/contents"
            headers = {"X-Dataverse-key": api_token}

            #Columnas de las tablas
            type_data = []  
            title_data = []
            doi_data = []
        
            try:
                response = requests.get(url, headers=headers)
                data = response.json() if response.status_code == 200 else {"error": "Failed to fetch data"}
                
                #IDS de datasets que componen la coleccion
                ids = [ val["id"] for val in data["data"]]
                print(ids)

                for val in data["data"]:
                    #doi_data.append(val["protocol"] +":" + val["authority"] + val["separator"] + val["identifier"])
                    doi_data.append(val["protocol"] +":" + val["authority"] + val["identifier"])
                    print(val)
                    


                for i in ids:

                    url_metadata_redgen = f"{server_url}/api/datasets/{i}/versions/:draft/metadata/redgen_metadata"
                    response_meta=requests.get(url_metadata_redgen, headers=headers)
                    type_data.append( response_meta.json()["data"]["fields"][1]["value"])

                    url_metadata_citation = f"{server_url}/api/datasets/{i}/versions/:draft/metadata/citation"
                    response_meta=requests.get(url_metadata_citation, headers=headers)
                    title_data.append( response_meta.json()["data"]["fields"][0]["value"])

                    #for j in data_f


            
                print(id)
            except Exception as e:
                data = {"error": str(e)}

            return render_template('my_template.html', list1=doi_data, list2 =title_data, list3=type_data, count=len(type_data))
        
        # @test_bp.route('/my_template.html')
        # def custom_route():

        #     list=['2', '3']
          
        #     return render_template('my_template.html', list1=list)


        return test_bp
    
    def before_map(self, map):
        # map.connect('home', '/', controller='ckanext.test.controller:TestController', action='index')
        map.connect('custom_route','/custom_route', controller='ckanext.test.controller:TestController', action='custom_route' )
        return map
    # IConfigurer
    
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
    
