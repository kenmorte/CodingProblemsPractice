# https://leetcode.com/problems/encode-and-decode-tinyurl/description/

class Codec:
    def __init__(self):
        self.encode_map = dict()
        self.decode_map = dict()

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.encode_map:
            return self.encode_map[longUrl]
        id = len(self.encode_map) + 1
        self.encode_map[longUrl] = id
        self.decode_map[id] = longUrl
        return str(id)
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        shortUrl = int(shortUrl)
        if shortUrl in self.decode_map:
            return self.decode_map[shortUrl]
        return ''
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
