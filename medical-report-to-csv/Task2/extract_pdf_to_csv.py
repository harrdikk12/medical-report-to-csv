import csv

try:
    with open('extracted_text.txt', 'r') as text_file:
        text = text_file.read()

    lines = text.strip().split('\n')
    print("Lines:", lines) 

    with open('output.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Test', 'Result', 'Unit', 'Biological Ref. Interval'])
        
        for line in lines:
            parts = line.split()
            
            if len(parts) >= 4:
                extra = parts[-2:]
                extra = extra[:1]
                test = ' '.join(parts[:1] + extra )
                result = parts[-1]
                
                unit = parts[1]
                oo = parts[2:6]
                
                ref_interval =' '.join([x for x in oo if x.replace('.', '', 1).isdigit() or x == '-'])
                
                csv_writer.writerow([test, result, unit, ref_interval])

    print("The text has been successfully converted to output.csv.")
except FileNotFoundError:
    print("Error: The file extracted_text.txt was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
