import json

def main() :
    with open('raw.txt', 'r', encoding="utf8") as file:
        raw = file.read().splitlines()
        data = {}

        for line in raw:
            line_split = list(filter(None, line.split(' ')))
            date  = line_split.pop(0)
            month = line_split.pop(0)
            event = ' '.join(line_split)
            
            if month in data:
                data[month].append({ 'date': date, 'event': event })
            else:
                data[month] = [ { 'date': date, 'event': event } ]

    formatted = json.dumps(data)
    with open('formatted.json', 'w') as file:
        file.write(formatted)

if __name__ == '__main__': main()