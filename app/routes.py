from app import app, db
from flask import redirect, render_template, request
from app.models import Interview
from datetime import date, datetime

@app.route('/')
def main():
    return render_template(
        'main_page.html'
    )

@app.route('/interviewer')
def interviewer():
    return render_template(
        'interviewer_page.html'
    )

@app.route('/interviewee', methods=['GET', 'POST'])
def interviewee():
    if request.method == 'GET':
        return render_template(
            'interviewee_page.html',
            table_head=[],
            table_content=[{}]
        )

    date = request.form.get('date_interviewee')
    language = request.form.get('language_interviewee')
    
    if not date or not language:
        return render_template(
            'error.html',
            message1='Something went wrong',
            message2='Make sure you enter valid data and try again'
        )
    
    date = datetime.strptime(date, '%Y-%m-%d').date()

    interviews = Interview.query.filter_by(date=date).all()
    table_content = []
    CHECKBOX_FLAG = 'radio_field'
    for interview in interviews:
        if language.lower() in interview.languages.lower():
            table_content.append(
                {'id' : interview.id,
                 'arr' : [interview.name, interview.languages, interview.date.strftime('%d %m %Y'), interview.hour, CHECKBOX_FLAG]}
            )

    table_head = ['Name', 'Languages', 'Date', 'Time', 'Check in']
    
    # table_content = [{ 'id' : '123123',
    #     'arr' :  ['George', 'Python, Java', '18-11-2024', '15:00-16:00', CHECKBOX_FLAG]
    # }]
    
    if table_content:
                    
        return render_template(
            'interviewee_page.html',
            table_head=table_head,
            table_content=table_content
        )
    else:

        return render_template(
            'error.html',
            message1='Nothing found for your request',
            message2='Wait until somebody add an interview in that period of time'
        )

@app.route('/submit', methods=['POST'])
def submit():
    
    formdata = dict(request.form)
    # check validity
    print(formdata)
    for key in ['telegram', 'name', 'date', 'hour', 'languages']:
        if not formdata[key]:
            return render_template(
                'error.html',
                message1='Something went wrong',
                message2='Make sure you enter valid data and try again'
            )
        
    formdata['telegram'] = formdata['telegram'].replace('@', '')
    
    datetime_obj = datetime.strptime(formdata['date'], '%Y-%m-%d')

    date_obj = datetime_obj.date()

    if datetime.today() > datetime_obj or not formdata['name'].isalpha():
        return render_template(
                'failed_to_add_interview.html'
            )   

    new_interview = Interview(
        name=formdata.get('name').strip(),
        telegram=formdata.get('telegram').strip(),
        date=date_obj,
        hour=formdata.get('hour').strip(),
        languages=formdata.get('languages')
    )
    try:
        db.session.add(new_interview)
        db.session.commit()
    except Exception as e:
        return render_template(
                'error.html',
                message1='Something went wrong',
                message2='Make sure you enter valid data and try again'
            )

    return render_template(
        'added_interview.html'
    )
@app.route('/record', methods=['POST'])
def recorded():

    id = request.form.get('radio')

    if not id:
        return 'WTF', 404
    
    interview = Interview.query.get(id)
    interviewer = {
        'name' : interview.name,
        'telegram' : '@' + interview.telegram
    }
    hour = interview.hour
    if 'pm' in hour:
        hour = hour.replace('pm', '')
        hour = str(int(hour) + 12)
    elif 'am' in hour:
        hour = hour.replace('am', '')

    hour = hour + ':00'

    interview_inf = {
        'date' : interview.date.strftime('%d.%m.%Y'),
        'hour' : hour
    }

    db.session.delete(interview)
    db.session.commit()

    return render_template(
        'succesfully_recorded.html',
        interviewer=interviewer,
        interview=interview_inf
    )