# Código simples para um chat-bot de atendimento.

responses = {
     
      "olá": "Olá! Bem-vindo ao Suporte Bot-suporte. Como posso ajudar hoje?",
      "você vende telefone celular?": "Sim, temos diversos modelos de telefones celulares. Você pode conferir na nossa página de produtos.",
      "qual o tempo de envio?": "O envio geralmente leva 3-5 dias úteis.",
      "quais os tipos de envio?": "Oferecemos envio padrão, expresso e noturno.",
      "posso devolver o produto?": "Você pode devolver produtos dentro de 30 dias após o recebimento para reembolso total.",
      "como faço para devolver o produto?": "Para devolver um produto, visite nossa página de devoluções para um guia passo a passo.",
      "meu produto não funiona": "Verifique se seu dispositivo está carregado. Se ainda não ligar, visite nossa página de solução de problemas.",
      "como resetar o dispositivo?": "Para resetar seu dispositivo, segure o botão de energia por 10 segundos. Se não funcionar, consulte o manual para reset de fábrica.",
      "bye": "Obrigado por contactar a Bot-suporte. Se tiver mais dúvidas, estamos à disposição. Até logo!"
}

def get_bot_response(user_input):
      user_input = user_input.lower()

      for keyword, response in responses.items():
          if keyword in user_input:
              return response

      return "Não tenho certeza de como responder isso. Você pode tentar perguntar de outra forma?"

while True:
      user_input = input("Você: ")
      if user_input.lower() in ["quit", "exit", "bye"]:
          print("Bot: Até logo! Se tiver mais alguma dúvida, estamos à disposição para ajudar.")
          break

      response = get_bot_response(user_input)
      print(f"Bot: {response}")