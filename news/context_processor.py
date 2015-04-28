__author__ = 'Алексей'

def custom_processor(request):
    return(
        {
            'custom_data' : 'Hello, World!',
        }
    )