import string
import random
import time

from .common import InfoExtractor


class DoodStreamIE(InfoExtractor):
    IE_NAME = 'DoodStream'
    _VALID_URL = r'https?://(?:www\.)?dood(s)?\.(?:to|com|watch|so|pm|wf|yt|pro|re|la|pm)/(?P<type>[ed])/(?P<id>[a-z0-9]+)'
    _TESTS = [{
        'url': 'http://dood.to/e/5s1wmbdacezb',
        'md5': '4568b83b31e13242b3f1ff96c55f0595',
        'info_dict': {
            'id': '5s1wmbdacezb',
            'ext': 'mp4',
            'title': 'Kat Wonders - Monthly May 2020',
            'description': 'Kat Wonders - Monthly May 2020 | DoodStream.com',
            'thumbnail': 'https://img.doodcdn.com/snaps/flyus84qgl2fsk4g.jpg',
        }
    }, {
        'url': 'http://dood.watch/d/5s1wmbdacezb',
        'md5': '4568b83b31e13242b3f1ff96c55f0595',
        'info_dict': {
            'id': '5s1wmbdacezb',
            'ext': 'mp4',
            'title': 'Kat Wonders - Monthly May 2020',
            'description': 'Kat Wonders - Monthly May 2020 | DoodStream.com',
            'thumbnail': 'https://img.doodcdn.com/snaps/flyus84qgl2fsk4g.jpg',
        }
    }, {
        'url': 'https://dood.to/d/jzrxn12t2s7n',
        'md5': '3207e199426eca7c2aa23c2872e6728a',
        'info_dict': {
            'id': 'jzrxn12t2s7n',
            'ext': 'mp4',
            'title': 'Stacy Cruz Cute ALLWAYSWELL',
            'description': 'Stacy Cruz Cute ALLWAYSWELL | DoodStream.com',
            'thumbnail': 'https://img.doodcdn.com/snaps/8edqd5nppkac3x8u.jpg',
        }
    }, {
        'url': 'https://dood.so/d/jzrxn12t2s7n',
        'only_matching': True
    }]

    def _real_extract(self, url):
        # video_id = self._match_id(url)
        video_id, url_type = self._match_valid_url(url).group('id', 'type')
        if url_type == 'd':
            webpage = self._download_webpage(url, video_id)
            video_id = self._html_search_regex(r'<iframe src="/e/(\w+)"', webpage, 'video_id')

        url = f'https://dood.to/e/{video_id}'
        webpage = self._download_webpage(url, video_id)

        title = self._html_search_meta(
            ('og:title', 'twitter:title'), webpage, default=None) or self._html_extract_title(webpage)
        thumb = self._html_search_meta(['og:image', 'twitter:image'], webpage, default=None)
        token = self._html_search_regex(r'[?&]token=([a-z0-9]+)[&\']', webpage, 'token')
        description = self._html_search_meta(
            ['og:description', 'description', 'twitter:description'], webpage, default=None)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/66.0',
            'referer': url
        }

        pass_md5 = self._html_search_regex(r'(/pass_md5.*?)\'', webpage, 'pass_md5')
        final_url = ''.join((
            self._download_webpage(f'https://dood.to{pass_md5}', video_id, headers=headers),
            *(random.choice(string.ascii_letters + string.digits) for _ in range(10)),
            f'?token={token}&expiry={int(time.time() * 1000)}',
        ))

        return {
            'id': video_id,
            'title': title,
            'url': final_url,
            'http_headers': headers,
            'ext': 'mp4',
            'description': description,
            'thumbnail': thumb,
        }


class Ds2playIE(InfoExtractor):
    IE_NAME = 'Doodstream-ds2play'
    _VALID_URL = r'https?://(?:www\.)?ds2play\.(?:com|to|watch|so|pm|wf|yt|pro|re|la|pm)/(?P<type>[ed])/(?P<id>[a-z0-9]+)'
    _TESTS = [{
        'url': 'http://ds2play.com/e/5s1wmbdacezb',
        'md5': '4568b83b31e13242b3f1ff96c55f0595',
        'info_dict': {
            'id': '5s1wmbdacezb',
            'ext': 'mp4',
            'title': 'Kat Wonders - Monthly May 2020',
            'description': 'Kat Wonders - Monthly May 2020 | DoodStream.com',
            'thumbnail': 'https://img.doodcdn.com/snaps/flyus84qgl2fsk4g.jpg',
        }
    }]

    def _real_extract(self, url):
        #video_id = self._match_id(url)
        video_id, url_type = self._match_valid_url(url).group('id', 'type')
        if url_type == 'd':
            webpage = self._download_webpage(url, video_id)
            video_id = self._html_search_regex(r'<iframe src="/e/(\w+)"', webpage, 'video_id')

        url = f'https://dood.to/e/{video_id}'
        webpage = self._download_webpage(url, video_id)

        title = self._html_search_meta(
            ('og:title', 'twitter:title'), webpage, default=None) or self._html_extract_title(webpage)
        thumb = self._html_search_meta(['og:image', 'twitter:image'], webpage, default=None)
        token = self._html_search_regex(r'[?&]token=([a-z0-9]+)[&\']', webpage, 'token')
        description = self._html_search_meta(
            ['og:description', 'description', 'twitter:description'], webpage, default=None)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/66.0',
            'referer': url
        }

        pass_md5 = self._html_search_regex(r'(/pass_md5.*?)\'', webpage, 'pass_md5')
        final_url = ''.join((
            self._download_webpage(f'https://dood.to{pass_md5}', video_id, headers=headers),
            *(random.choice(string.ascii_letters + string.digits) for _ in range(10)),
            f'?token={token}&expiry={int(time.time() * 1000)}',
        ))

        return {
            'id': video_id,
            'title': title,
            'url': final_url,
            'http_headers': headers,
            'ext': 'mp4',
            'description': description,
            'thumbnail': thumb,
        }

class DoodMainIE(InfoExtractor):
    IE_NAME = 'Doodstream-main'
    _VALID_URL = r'https?://(?:www\.)?(?:do0od|doodstream|d0o0d|dooood)\.com/(?P<type>[ed])/(?P<id>[a-z0-9]+)'
    _TESTS = [{
        'url': 'http://dooood.com/e/5s1wmbdacezb',
        'md5': '4568b83b31e13242b3f1ff96c55f0595',
        'info_dict': {
            'id': '5s1wmbdacezb',
            'ext': 'mp4',
            'title': 'Kat Wonders - Monthly May 2020',
            'description': 'Kat Wonders - Monthly May 2020 | DoodStream.com',
            'thumbnail': 'https://img.doodcdn.com/snaps/flyus84qgl2fsk4g.jpg',
        }
    }]

    def _real_extract(self, url):
        #video_id = self._match_id(url)
        video_id, url_type = self._match_valid_url(url).group('id', 'type')
        if url_type == 'd':
            webpage = self._download_webpage(url, video_id)
            video_id = self._html_search_regex(r'<iframe src="/e/(\w+)"', webpage, 'video_id')

        url = f'https://dood.to/e/{video_id}'
        webpage = self._download_webpage(url, video_id)

        title = self._html_search_meta(
            ('og:title', 'twitter:title'), webpage, default=None) or self._html_extract_title(webpage)
        thumb = self._html_search_meta(['og:image', 'twitter:image'], webpage, default=None)
        token = self._html_search_regex(r'[?&]token=([a-z0-9]+)[&\']', webpage, 'token')
        description = self._html_search_meta(
            ['og:description', 'description', 'twitter:description'], webpage, default=None)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/66.0',
            'referer': url
        }

        pass_md5 = self._html_search_regex(r'(/pass_md5.*?)\'', webpage, 'pass_md5')
        final_url = ''.join((
            self._download_webpage(f'https://dood.to{pass_md5}', video_id, headers=headers),
            *(random.choice(string.ascii_letters + string.digits) for _ in range(10)),
            f'?token={token}&expiry={int(time.time() * 1000)}',
        ))

        return {
            'id': video_id,
            'title': title,
            'url': final_url,
            'http_headers': headers,
            'ext': 'mp4',
            'description': description,
            'thumbnail': thumb,
        }
class DoodPatchIE(InfoExtractor):
    IE_NAME = 'Doodstream-pt'
    _VALID_URL = r'https?://d.*d.*\.*(to|com|watch|so|pm|wf|yt|pro|re|la|pm).*'
    _TESTS = [{
        'url': 'http://dooood.com/e/5s1wmbdacezb',
        'md5': '4568b83b31e13242b3f1ff96c55f0595',
        'info_dict': {
            'id': '5s1wmbdacezb',
            'ext': 'mp4',
            'title': 'Kat Wonders - Monthly May 2020',
            'description': 'Kat Wonders - Monthly May 2020 | DoodStream.com',
            'thumbnail': 'https://img.doodcdn.com/snaps/flyus84qgl2fsk4g.jpg',
        }
    }]

    def _real_extract(self, url):
        # video_id = self._match_id(url)
        video_id, url_type = self._match_valid_url(url).group('id', 'type')
        if url_type == 'd':
            webpage = self._download_webpage(url, video_id)
            video_id = self._html_search_regex(r'<iframe src="/e/(\w+)"', webpage, 'video_id')

        url = f'https://dood.to/e/{video_id}'
        webpage = self._download_webpage(url, video_id)

        title = self._html_search_meta(
            ('og:title', 'twitter:title'), webpage, default=None) or self._html_extract_title(webpage)
        thumb = self._html_search_meta(['og:image', 'twitter:image'], webpage, default=None)
        token = self._html_search_regex(r'[?&]token=([a-z0-9]+)[&\']', webpage, 'token')
        description = self._html_search_meta(
            ['og:description', 'description', 'twitter:description'], webpage, default=None)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/66.0',
            'referer': url
        }

        pass_md5 = self._html_search_regex(r'(/pass_md5.*?)\'', webpage, 'pass_md5')
        final_url = ''.join((
            self._download_webpage(f'https://dood.to{pass_md5}', video_id, headers=headers),
            *(random.choice(string.ascii_letters + string.digits) for _ in range(10)),
            f'?token={token}&expiry={int(time.time() * 1000)}',
        ))

        return {
            'id': video_id,
            'title': title,
            'url': final_url,
            'http_headers': headers,
            'ext': 'mp4',
            'description': description,
            'thumbnail': thumb,
        }


