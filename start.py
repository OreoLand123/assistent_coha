
from assistent.main import recognize, vectorizer, clf
import threading
import asyncio
from func_assistent.base_func.record_voice import voice_func
from func_assistent.base_func.voice import speaker
from func_assistent.tg_func.push_notifications import app




def assistent_main():
    speaker("Приветствую, к-оха готова к работе")
    while True:
        data = voice_func()
        recognize(data, vectorizer, clf)

def assistent():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(future=assistent_main())


def run_app():
    threading.Thread(target=assistent_main).start()
    app.run()

if __name__ == '__main__':
    run_app()