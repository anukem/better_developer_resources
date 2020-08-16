# # Given a string s,
# find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.

# Example 1
# Input: "babad"
# Output: "bab", or "aba"

# Example 2
# Input: "cbbd"
# Output: "bb"


# too_close() => bool whether or not a char is too close to be considered
# is_palindrome() bool whether or not the string it gets is a palindrome
# find_next_letter() returns the index of the next similar letter or nil

def too_close(string, beginning, ending, possible)
  ending - beginning > possible - ending
end

def find_next_letter string, char
  the_index = string.index(char) + 1
  begin
    string[the_index, string.length - 1].index(char) + 1
  rescue
    nil
  end
end




# 1. find the next letter if there is one => index or nil
#   1. check if theres a palindrome from current_index to next_letter
#     1. if there is then search for the next_letter
#       1. if the next_letter is far enough check for a palindrome from current letter to there
#       2. if the next letter is too close, look for the next_letter
#       3. if it doesnt exist

def find_longest_palindromic_substring s


  array_of_indicies = []
  for num in 0...s.length
    array_of_indicies.push(num)
  end

  for position in array_of_indicies
    next_matching_char_index = find_next_letter(s[position, s.length], s[position])
    if next_matching_char_index
      puts s[position, next_matching_char_index + 1]
      possible_palindrome = s[position, next_matching_char_index + 1]
      if is_palindrome(possible_palindrome)
        puts "made it here"
        rest_of_the_string = s[next_matching_char_index + 1, s.length]
        # next_char_index = find_next_letter()
        puts rest_of_the_string
      end
    end
  end
end

def is_palindrome s
  left = 0
  right = 0
  if s.length % 2 == 0
    left = s.length/2 - 1
    right = s.length/2
  else
    left = s.length/2 - 1
    right = s.length/2 + 1
  end

  while right < s.length and left > -1
    if s[left] == s[right]
      left -= 1
      right += 1
      next
    else
      return false
    end
  end
  true
end


# puts find_longest_palindromic_substring "ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy"
# puts find_longest_palindromic_substring "anugnxshgonmqydttcvmtsoaprxnhpmpovdolbidqiyqubirkvhwppcdyeouvgedccipsvnobrccbndzjdbgxkzdbcjsjjovnhpnbkurxqfupiprpbiwqdnwaqvjbqoaqzkqgdxkfczdkznqxvupdmnyiidqpnbvgjraszbvvztpapxmomnghfaywkzlrupvjpcvascgvstqmvuveiiixjmdofdwyvhgkydrnfuojhzulhobyhtsxmcovwmamjwljioevhafdlpjpmqstguqhrhvsdvinphejfbdvrvabthpyyphyqharjvzriosrdnwmaxtgriivdqlmugtagvsoylqfwhjpmjxcysfujdvcqovxabjdbvyvembfpahvyoybdhweikcgnzrdqlzusgoobysfmlzifwjzlazuepimhbgkrfimmemhayxeqxynewcnynmgyjcwrpqnayvxoebgyjusppfpsfeonfwnbsdonucaipoafavmlrrlplnnbsaghbawooabsjndqnvruuwvllpvvhuepmqtprgktnwxmflmmbifbbsfthbeafseqrgwnwjxkkcqgbucwusjdipxuekanzwimuizqynaxrvicyzjhulqjshtsqswehnozehmbsdmacciflcgsrlyhjukpvosptmsjfteoimtewkrivdllqiotvtrubgkfcacvgqzxjmhmmqlikrtfrurltgtcreafcgisjpvasiwmhcofqkcteudgjoqqmtucnwcocsoiqtfuoazxdayricnmwcg"
# puts find_longest_palindromic_substring "rbbr"
puts find_longest_palindromic_substring "rbebr"
