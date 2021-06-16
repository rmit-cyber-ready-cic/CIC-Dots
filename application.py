from flask import Flask
from flask import render_template

application = Flask(__name__)


@application.route('/dashboard')
def index():
    return render_template("dashboard.html")


@application.route('/')
def login():
    return render_template("login.html")


@application.route('/asset360')
def asset360():
    return render_template("asset360.html")


@application.route('/test')
def test():
    return render_template("test.html")


@application.route('/alarms')
def alarms():
    return render_template("alarms.html")


@application.route('/knowledgebase_videos')
def knowledge_base_videos():
    return render_template("knowledgebase_videos.html")


@application.route('/knowledgebase_instructions')
def knowledge_base_instructions():
    return render_template("knowledgebase_instructions.html")


@application.route('/task_unplanned')
def task_unplanned():
    data = [{'wo_number':'953042', 'date_assigned':'20/4/2021', 'description':'Lighting out','site':'MoL - Docklands','asset_id': '', 'skillset': 'Lighting', 'assigned_to': 'John'},
    {'wo_number':'952992', 'date_assigned':'20/4/2021', 'description':'Emergency Light Remedials','site':'MoL - Docklands','asset_id': '', 'skillset': '', 'assigned_to': 'John'},
    {'wo_number':'950615', 'date_assigned':'30/3/2021', 'description':'AHU 6 Bearing Replaceemnt ATON 363','site':'MoL - Docklands','asset_id': 'AHU06', 'skillset': 'Quote Request', 'assigned_to': 'Steve'},
    {'wo_number':'950273', 'date_assigned':'26/3/2021', 'description':'Lighting out','site':'MoL - Docklands','asset_id': '', 'skillset': '', 'assigned_to': 'Steve'},
    {'wo_number':'949208', 'date_assigned':'18/3/2021', 'description':'Hand dryer broken','site':'MoL - Docklands','asset_id': '', 'skillset': 'Handyman / Fab Tech', 'assigned_to': 'Steve'},
    {'wo_number':'948320', 'date_assigned':'11/3/2021', 'description':'Lighting out','site':'MoL - Docklands','asset_id': '', 'skillset': 'Lighting', 'assigned_to': 'Steve'},
    {'wo_number':'947411', 'date_assigned':'03/3/2021', 'description':'Leaking pipe','site':'MoL - Docklands','asset_id': 'AHU01', 'skillset': 'Mechanical / Plumbing', 'assigned_to': 'Steve'},
    {'wo_number':'946260', 'date_assigned':'21/2/2021', 'description':'Lighting out','site':'MoL - Docklands','asset_id': '', 'skillset': '', 'assigned_to': 'Steve'},
    {'wo_number':'946005', 'date_assigned':'18/2/2021', 'description':'BMS System Upgrade Works','site':'MoL - Docklands','asset_id': '', 'skillset': 'Sub-contractor', 'assigned_to': 'John'},
    {'wo_number':'945900', 'date_assigned':'18/2/2021', 'description':'ATON 356 Install Vision panels for Mudlarks Fire ','site':'MoL - Docklands','asset_id': '', 'skillset': 'Quote Request', 'assigned_to': 'John'},
    {'wo_number':'945686', 'date_assigned':'16/2/2021', 'description':'Emergency Light replacement Batteries','site':'MoL - Docklands','asset_id': '', 'skillset': 'Electrical', 'assigned_to': 'John'},
    {'wo_number':'944638', 'date_assigned':'05/2/2021', 'description':'Alarm in comms room','site':'MoL - Docklands','asset_id': 'AHU01', 'skillset': 'Electrical', 'assigned_to': 'John'},
    {'wo_number':'943893', 'date_assigned':'29/1/2021', 'description':'replace faulty smoke head Plant room 5','site':'MoL - Docklands','asset_id': '', 'skillset': '', 'assigned_to': 'John'},
    {'wo_number':'943140', 'date_assigned':'22/1/2021', 'description':'Quote for repairs to AHU 12 Humidifier','site':'MoL - Docklands','asset_id': 'AHU12', 'skillset': 'Sub-contractor', 'assigned_to': 'John'}]
    return render_template("task_unplanned.html", data = data)


@application.route('/task_planned')
def task_planned():
    data = [{'wo_number':'946005', 'date_assigned':'18/2/2021', 'description':'BMS System Upgrade Works','site':'MoL - Docklands','asset_id': '', 'skillset': 'Sub-contractor', 'assigned_to': 'John'},]
    return render_template("task_planned.html", data=data)


@application.route('/model3d')
def model3d():
    return render_template("model3d.html")


if __name__ == "__main__":
    application.run(debug=True)
