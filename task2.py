import re

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxgc'
#line = 'abc'
line_data = list(line)
print("Исходная строка", line, "Количество символов = ", len(line_data))


print("Задание 2.1")
n = (len(line_data))
line_data_reg = []
if line_data[1].islower == False: # только для 1го символа
    line_data_reg.append(line_data[0])
for i in range(1, n-1):
    if line_data[i].islower():
        if line_data[i-1].islower() == False or line_data[i+1].islower() == False:
            line_data_reg.append(line_data[i])
if line_data[len(line_data)-1].islower == False: # только для последнего символа
    line_data_reg.append(line_data[len(line_data)-2])
print("Символы нижнего регистра, которых окружают 1 или более символов верхнего регистра: ", line_data_reg)


print("Задание 2.2")
n = (len(line_data))
line_data_reg = []
for i in range(2, n-2):
    if line_data[i].islower() == False:
        if line_data[i-2].islower() and line_data[i-1].islower() and line_data[i+1].islower() == False and line_data[i+2].islower() == False:
            line_data_reg.append(line_data[i])
print("Символы верхнего регистра, которых окружают 2 символа нижнего регистра слева и 2 символа верхнего регистра справа: ", line_data_reg)


print("Задание 2.3")
file1 = []
file2 = []
file3 = []
file4 = []
file5 = []

for i in range(0, n, 5):
    file1.append(line_data[i])
f = open("file_1.txt", "w")
f.write("".join(file1))
f.close

for i in range(1, n, 5):
    file2.append(line_data[i])
f = open("file_2.txt", "w")
f.write("".join(file2))
f.close

for i in range(2, n, 5):
    file3.append(line_data[i])
f = open("file_3.txt", "w")
f.write("".join(file3))
f.close

for i in range(3, n, 5):
    file4.append(line_data[i])
f = open("file_4.txt", "w")
f.write("".join(file4))
f.close

for i in range(4, n, 5):
    file5.append(line_data[i])
f = open("file_5.txt", "w")
f.write("".join(file5))
f.close

print("Строка записана в файлы в рабочей директории")
