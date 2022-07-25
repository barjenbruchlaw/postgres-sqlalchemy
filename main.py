from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = "postgresql://postgres:Barton1993!@localhost:5432/docket_manager"

db = create_engine(db_string)

base = declarative_base()

class Template(base):
    __tablename__='templates'
    template_id = Column(Integer, primary_key=True)
    template_path = Column(String)
    template_name = Column(String)
    output_filename = Column(String)
    update_paragraph_runs = Column(JSON)
    update_table_runs = Column(JSON)

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

# message_template = Template(
#         template_path="message-template.docx",
#         template_name="message",
#         output_filename='message_{{datetimestamp}}.docx',
#         update_paragraph_runs=[{"{{name}}": "Brian Barjenbruch"},
#                                {"{{datetimestamp}}": "2022-07-25_103330"},
#                                {"{{message}}": "Hello world!"}])
# session.add(message_template)
# session.commit()

templates = session.query(Template)
for template in templates:
    print(template.template_id, template.template_name, template.update_paragraph_runs[1].values())
