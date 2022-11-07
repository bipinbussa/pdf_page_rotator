from flask import Flask
from flask_restful import Api,Resource,reqparse
import PyPDF2
pdf_put_args=reqparse.RequestParser()
pdf_put_args.add_argument("path",type=str)
pdf_put_args.add_argument("angle",type=int)
pdf_put_args.add_argument("page_number",type=int)


app=Flask(__name__)
api=Api(app)
class Rotate(Resource):
    def put(self):
        args=pdf_put_args.parse_args()
        pdf_in = open(args["path"], 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_in)
        pdf_writer = PyPDF2.PdfFileWriter()

        for pagenum in range(pdf_reader.numPages):
            page = pdf_reader.getPage(pagenum)
            if pagenum == args["page_number"]-1:
                page.rotateClockwise(args["angle"])
            pdf_writer.addPage(page)

        pdf_out = open('rotated.pdf', 'wb')
        pdf_writer.write(pdf_out)
        pdf_out.close()
        pdf_in.close()
        return {"process":"success"}
        

api.add_resource(Rotate,"/pdf")
if __name__=="__main__":
    app.run(debug=True)
    
    
