
lexicon = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction',
    'west': 'direction',
    'down': 'direction',
    'up': 'direction',
    'left': 'direction',
    'right': 'direction',
    'back': 'direction',
    'go': 'verb',
    'stop': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    'from': 'stop',
    'at': 'stop',
    'it': 'stop',
    'door': 'noun',
    'bear': 'noun',
    'princess': 'noun',
    'cabinet': 'noun',
    }
    

def scan(sentence):
    words = sentence.split(' ')
    result = []
    for word in words:
        try:
            result.append(('number', int(word)))
        except ValueError:
            try:
                result.append((lexicon[word], word))
            except KeyError:
                result.append(('error', word))
    return result







