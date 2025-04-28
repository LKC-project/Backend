from didiator import Mediator

from src.application.chat.commands.send_prompt import SendPrompt, SendPromptHandler


def setup_chat_handlers(mediator: Mediator):
    mediator.register_command_handler(SendPrompt, SendPromptHandler)
