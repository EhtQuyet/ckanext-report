from flask import  send_file, Response
import io 
import xlwt
import wget
from ckan import model
from ckan.lib import helpers


def test_download():

   try:
      data1 = model.User.all()
      data2 = helpers.organizations_available()
      print('data2', data2)
      data_table = [
        {'name': 'Bảng thông tin', 'views': '1903', 'value': '$10', 'bounce_rate': '50%'},
        {'name': 'Form admin', 'views': '123', 'value': '0', 'bounce_rate': '64%'},
        {'name': 'Util admin', 'views': '534', 'value': '$245', 'bounce_rate': '34%'},
        {'name': 'Validation', 'views': '567', 'value': '$103', 'bounce_rate': '23%'},
        {'name': 'Modals', 'views': '796', 'value': '$19', 'bounce_rate': '43%'},
      ]

      output = io.BytesIO()
      workbook = xlwt.Workbook()
      sh = workbook.add_sheet('Test')

      sh.write(0, 0, 'Name')
      sh.write(0, 1, 'Views')
      sh.write(0, 2, 'Value')
      sh.write(0, 3, 'Bounce Rate')
      
      idx = 0
      for row in data_table:
         sh.write(idx+1, 0, row['name'])
         sh.write(idx+1, 1, row['views'])
         sh.write(idx+1, 2, row['value'])
         sh.write(idx+1, 3, row['bounce_rate'])
         idx+=1

      workbook.save(output)
      output.seek(0)
      # print('output', output)
      # url = "https://www.python.org/static/img/python-logo@2x.png"
      # wget.download(url)
      return Response(output, mimetype="application/ms-excel", headers={"Content-Disposition":"attachment;filename=student_report.xls"})

      # return send_file(output, attachment_filename="testing.xlsx", as_attachment=True)

   except Exception as e:
      print(e, '111111111')

