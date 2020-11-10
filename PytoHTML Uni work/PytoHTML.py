def Table_Start():
    fileout = open("SmokeResults.html", "w")
    table = """
    <!DOCTYPE html>
    <html>
    <head>
    <title>*TEST* Athena UI Results</title>
    <style>
    table {
      font-family: arial;
      border-collapse: collapse;
      width: 350px;
    }
    td, th {
      border: 1px solid #000000;
      text-align: left;
      padding: 10px;
    }

    tr:nth-child(odd) {
      background-color: #eeeeee;
    }
    </style>
    </head>

    <body>
    """
    fileout.writelines(table)
    fileout.close()       

def Table_html(filename, TestName):
    
    filein = open(filename, "r")
    fileout = open("SmokeResults.html", "a")
    data = filein.readlines()
    table = '<h2 style="font-size:20px;">' + TestName + '</h2>'    

    table += '''
    <table class="fixed">
        <col width="20px" />
        <col width="30px" />
        <col width="40px" />
    '''

    header = data[0].split(":")
    table += "  <tr>\n"


    for column in header:
        table += '    <th style="font-size:15px;" style="background-color:powderblue;">{0}</th>\n'.format(column.strip())
    table += "  </tr>\n"

    # Create the table's row data
    for line in data[1:]:
        row = line.split(":")
        table += '<tr>\n'    
        for column in row:
            #add another loop - green or red
            if "Pass" in column and row:
                table += '    <td style="color:green;">{0}</td>\n'.format(column.strip())
            elif "Fail" in column and row:
                table += '    <td style="color:red;">{0}</td>\n'.format(column.strip())
            else:
                table += '    <th style="font-size:15px;">{0}</th>'.format(column.strip())
        table += "  </tr>\n" 

    table += "</table>"

    fileout.writelines(table)
    fileout.close()
    filein.close() 

