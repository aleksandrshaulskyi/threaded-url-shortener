from infrastructure.callbacks import shortening_callback
from infrastructure.executor import executor
from infrastructure.tasks import process


def run() -> None:
    """
    Just a runner that is constantly listening to user inputs.
    """
    try:
        while True:
            message = (
                '''
                Type or paste a comma separated procedure code and a url that needs to be shortened.
                Procedure code should be either s or r letter depending on whether you wish to get
                a shortened version of a url or retrieve it's full counterpart.
                '''
            )
            print(message)
            user_input = input()

            future = executor.executor.submit(process, user_input)
            future.add_done_callback(shortening_callback)
    except KeyboardInterrupt:
        executor.stop()
        print('The executor was stopped.')

if __name__ == '__main__':
    run()
