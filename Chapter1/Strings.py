# -*- coding:utf-8 -*-
# @Time     :2019/8/10 18:41
# @Author   :chendaiwu_biubiubiu-----
# @FileName :Strings.py
# @Sofaware :PyCharm

#字符串
print("Output #14: {0:s}".format('I\'m enjoying learning python.'))
print("Output #15: {0:s}".format("This is a long string. Without the backslash "
                                 "it would run off of the page on the right in the text editor and be very "
                                 "difficult to read and edit. By using the backslash you can split the long "
                                 "string into smaller string on separate lines so that the whole strig is easy "
                                 "to view in the text editor."))
print("Output #16: {0:s}".format('''You can use triplr single quotes
for multi-line comment string.'''))
print("Output #17: {0:s}".format("""You can use triplr single quotes
for multi-line comment string."""))

string1 = "This is a "
string2 = "short string,"
sentence = string1 + string2
print("Output #18: {0:s}".format(sentence))
print("Output #19: {0:s} {1:s} {2:s}".format("She is", "very "*4, "beautiful"))
m = len(sentence)
print("Output #20: {0:d}".format(m))

#split
string1 = "My deliverable is due in May"
string1_list1 = string1.split()
string1_list2 = string1.split(" ",2)
print("Output #21: {0}".format(string1_list1))
print("Output #22: FIRST PIECE:{0} SECOND PIECE:{1} THIRD PIECE:{2}".format(string1_list2[0], string1_list2[1],string1_list2[2]))
string2 = "Your,deliverable,is,due,in,June"
string2_list = string2.split(',')
print("Output #23: {0}".format(string2_list))
print("Output #24: {0} {1} {2}".format(string2_list[1], string2_list[5], string2_list[-1]))

#join
print("Output #25: {0}".format(','.join(string2_list)))

#strip
string3 = "   Remove unwanted characters    from this string.\t\t   \n"
print("Output #26: string3:{0:s}".format(string3))
string3_lstrip = string3.lstrip()
print("Output #27: lstrip: {0:s}".format(string3_lstrip))
string3_rstrip = string3.rstrip()
print("Output #28: rstrip: {0:s}".format(string3_rstrip))
string3_strip = string3.strip()
print("Output #29: strip: {0:s}".format(string3_strip))
string4 = "$$Here's another string that has unwanted characeters.__---++"
print("Output #30: {0:s}".format(string4))
string4_strip = string4.strip('$_-+')
print("Output #31: {0:s}".format(string4_strip))

#replace
string5 = "Let's replace the spaces in this senetence with other characters."
string5_replace = string5.replace(" ","!@!")
print("Output #32: (with !@!): {0:s}".format(string5_replace))
string5_replace = string5.replace(" ", ",")
print("Output #33: (with commas) {0:s}".format(string5_replace))

#lower、upper、capitalize 字母大小写之间的转换，对字符串的首字母大写，其余小写
string6 = "Here's WHAT Happens WHEN You Use lower."
print("Output #34: {0:s}".format(string6.lower()))
string7 = "Here's what Happens when You Use UPPER."
print("Output #35: {0:s}".format(string7.upper()))
string8 = "here's WHAT happens WHEN you use Capitalize."
print("Output #36: {0:s}".format(string8.capitalize()))
string8_list = string8.split()
print("Output #37 (on each word):")
for word in string8_list:
    print("{0:s}".format(word.capitalize()))