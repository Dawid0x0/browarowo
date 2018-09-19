from brewery import tool
from string import ascii_lowercase


class TestTool:
    
    def test_random_slug(self):
        slug = 'test-slug'
        random_out = tool.random_slug(slug)
        random_str = random_out[-4:]
        assert type(random_str) == unicode, 'Should return string gen'
        assert random_out == '%s-%s' %(slug,random_str), 'Should return slug gen'