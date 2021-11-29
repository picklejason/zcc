from zenpy import Zenpy
import os
from dotenv import load_dotenv

load_dotenv()

def login(email, token, subdomain):

  creds = {
      'email' : email,
      'token' : token,
      'subdomain': subdomain
  }

  return Zenpy(**creds)

def login_status():
  try:
    login(os.environ.get("EMAIL"), os.environ.get("TOKEN"), os.environ.get("SUBDOMAIN")).tickets()
  except Exception as e:
    return 0
  return 1

def get_tickets(client):
  ticket_generator = client.tickets()
  tickets = list(ticket_generator)

  return tickets

def ticket_viewer(client):
  tickets = get_tickets(client)
  index = 0
  print("----------------------------")
  print("Welcome to the ticket viewer")
  print("----------------------------")
  status = True
  num_tickets = len(tickets)
  while status:
    inp = input("Type \'menu\' to view options or \'quit\' to exit\n")

    if inp == 'menu':
      option = input("Select view options:\n\t* Press 1 to view all tickets\n\t* Press 2 to view a ticket\n\t* Type 'quit' to exit\n")

      if option == '1':
        for ticket in tickets[index:index+25]:
          print(f"{int(ticket.id) - 1} | \'{ticket.subject}\' opened by {ticket.requester.name} on {ticket.created}")
        
        if num_tickets > 25:
          while status and index + 25 < num_tickets:
            page = input("Type \'n\' to go to the next page or \'b\' to go back\n")

            if page == 'n':
              index += 25
              if index + 25 > num_tickets:
                page_tickets = tickets[index:]
              else:
                page_tickets = tickets[index:index+25]
              
              for ticket in page_tickets:
                print(f"{int(ticket.id) - 1} | \'{ticket.subject}\' opened by {ticket.requester.name} on {ticket.created}")
            elif page == 'quit':
              status = False
            elif page == 'b':
              break

      elif option == '2':

        try:
          ticket_num = input("Enter ticket number:\n")
          print(f"Requester: {tickets[int(ticket_num) - 1].requester.name}\nSubject: {tickets[int(ticket_num) - 1].subject}\n{tickets[int(ticket_num) - 1].description}\n")
        except IndexError:
          print("Ticket not Found.")

      elif option == 'quit':
        status = False
    else:
      status = False

if __name__ == "__main__":
  zenpy_client = login(os.environ.get("EMAIL"), os.environ.get("TOKEN"), os.environ.get("SUBDOMAIN"))
  ticket_viewer(zenpy_client)
