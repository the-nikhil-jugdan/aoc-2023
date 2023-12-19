import re

one_to_nine = ["zero", "one", "two" ,"three", "four", "five", "six", "seven", "eight", "nine"]
rev = [i[::-1] for i in one_to_nine]
s_to_i = {
        ind:str(i) for i,ind in enumerate( one_to_nine )
}

sum = 0

numeric_regex = "|".join([ f"{i}" for i in range(0,10)])

straight_regex = "|".join([]+one_to_nine)

reverse_regex = "|".join([] + [ i[::-1] for i in one_to_nine])

numeric_regex = re.compile(numeric_regex)
straight_regex = re.compile(straight_regex)
reverse_regex = re.compile(reverse_regex)
with(open("input.txt", "r")) as f:
    x = f.readline()
    while x:
        if x is not None:
            x = x.strip()
            match =  straight_regex.search(x)
            if match:
                start = match.start()
                end =  match.end()
                x = x[:start] + s_to_i[x[start:end]] + x[start:]
            x = x[::-1]
            match = reverse_regex.search(x)
            if match:
                start = match.start()
                end = match.end()
                x = x[:start] + s_to_i[x[start:end][::-1]] + x[start:]
            x = x[::-1]
            a = int(numeric_regex.search(x)[0])
            b = int(numeric_regex.search(x[::-1])[0])
            sum += a * 10 + b
        x = f.readline()
print(sum)
