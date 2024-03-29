#!env/bin/python


import imp
from migrate.versioning import api
from app import db
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO


migration = SQLALCHEMY_MIGRATE_REPO + '/versions/%03d_migration.py' % (api.db_version(
                        SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO) + 1)
tmp_module = imp.new_module('old_model')
old_module = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
exec old_module in tmp_module.__dict__
script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI,
                        SQLALCHEMY_MIGRATE_REPO, tmp_module.meta, db.metadata)
open(migration, 'wt').write(script)
a = api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print "New migration saved as " + migration
print "Current Databae version: " + str(api.db_version(
                                SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO))
