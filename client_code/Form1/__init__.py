from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

resp = anvil.server.call('conect_mongoDB')

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_login_click(self, **event_args):
    user_name = self.name.text
    user_password = self.password.text
    if user_name != "" and user_password != "":
      alert(f"Hola, {user_name}")
    else:
      alert("Access denied")

  def button_create_click(self, **event_args):
    user_name = self.name.text
    user_password = self.password.text
    resp = anvil.server.call('create_user', user_name, user_password)
    if resp:
      alert(f"El usuario {user_name} ha sido creado")

