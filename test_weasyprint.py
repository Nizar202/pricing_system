from weasyprint import HTML

HTML(string='<h1>Hello, world!</h1>').write_pdf('hello.pdf')
