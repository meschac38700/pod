# -*- coding: utf-8 -*-
"""
Copyright (C) 2015 Remi Kroll review by Nicolas Can
Ce programme est un logiciel libre : vous pouvez
le redistribuer et/ou le modifier sous les termes
de la licence GNU Public Licence telle que publiée
par la Free Software Foundation, soit dans la
version 3 de la licence, ou (selon votre choix)
toute version ultérieure.
Ce programme est distribué avec l'espoir
qu'il sera utile, mais SANS AUCUNE
GARANTIE : sans même les garanties
implicites de VALEUR MARCHANDE ou
D'APPLICABILITÉ À UN BUT PRÉCIS. Voir
la licence GNU General Public License
pour plus de détails.
Vous devriez avoir reçu une copie de la licence
GNU General Public Licence
avec ce programme. Si ce n'est pas le cas,
voir http://www.gnu.org/licenses/
"""
from django.core.files import File
from core.models import *
from django.conf import settings
from django.test import TestCase, override_settings
from django.utils import timezone
from pods.models import *
from django.core.files.temp import NamedTemporaryFile
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User, Group
from filer.models.imagemodels import Image
from django.test import Client
from django.test.client import RequestFactory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date, timedelta
import os
from django.db.models import Count

RSS = getattr(settings, 'RSS', False)

# Create your tests here.
"""
    test the channel
"""


@override_settings(
    MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'media'),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite',
        }
    }
)
class ChannelTestCase(TestCase):
    fixtures = ['initial_data.json', ]

    def setUp(self):
        Channel.objects.create(title="ChannelTest1", slug="blabla")
        Channel.objects.create(title="ChannelTest2", visible=True,
                               color="Black", style="italic", description="blabla")

        print(" --->  SetUp of ChannelTestCase : OK !")
    """
		test all attributs when a channel have been save with the minimum of attributs
	"""

    def test_Channel_null_attribut(self):
        channel = Channel.objects.annotate(video_count=Count(
            "pod", distinct=True)).get(title="ChannelTest1")
        self.assertEqual(channel.visible, False)
        self.assertFalse(channel.slug == slugify("blabla"))
        self.assertEqual(channel.color, None)
        self.assertEqual(channel.description, '')
        self.assertEqual(channel.headband, None)
        self.assertEqual(channel.style, None)
        self.assertEqual(channel.__unicode__(), 'ChannelTest1')
        self.assertEqual(channel.video_count, 0)
        self.assertEqual(channel.get_absolute_url(), "/" + channel.slug + "/")

        print(
            "   --->  test_Channel_null_attribut of ChannelTestCase : OK !")

    """
		test attributs when a channel have many attributs
	"""

    def test_Channel_with_attributs(self):
        channel = Channel.objects.annotate(video_count=Count(
            "pod", distinct=True)).get(title="ChannelTest2")
        self.assertEqual(channel.visible, True)
        channel.color = "Blue"
        self.assertEqual(channel.color, "Blue")
        self.assertEqual(channel.description, 'blabla')
        self.assertEqual(channel.headband, None)
        self.assertEqual(channel.style, "italic")
        self.assertEqual(channel.__unicode__(), 'ChannelTest2')
        self.assertEqual(channel.video_count, 0)
        self.assertEqual(channel.get_absolute_url(), "/" + channel.slug + "/")

        print(
            "   --->  test_Channel_with_attributs of ChannelTestCase : OK !")

    """
        test delete object
    """

    def test_delete_object(self):
        Channel.objects.get(id=1).delete()
        Channel.objects.get(id=2).delete()
        self.assertEquals(Channel.objects.all().count(), 0)

        print(
            "   --->  test_delete_object of ChannelTestCase : OK !")

"""
	test the theme
"""


@override_settings(
    MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'media'),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite',
        }
    },
    LANGUAGE_CODE='en'
)
class ThemeTestCase(TestCase):
    fixtures = ['initial_data.json', ]

    def setUp(self):
        Channel.objects.create(title="ChannelTest1")
        Theme.objects.create(
            title="Theme1", slug="blabla", channel=Channel.objects.get(title="ChannelTest1"))

        print(" --->  SetUp of ThemeTestCase : OK !")

    """
		test all attributs when a theme have been save with the minimum of attributs
	"""

    def test_Theme_null_attribut(self):
        theme = Theme.objects.annotate(video_count=Count(
            "pod", distinct=True)).get(title="Theme1")
        self.assertFalse(theme.slug == slugify("blabla"))
        self.assertEqual(theme.headband, None)
        self.assertEqual(theme.__unicode__(), "ChannelTest1: Theme1")
        self.assertEqual(theme.video_count, 0)
        self.assertEqual(theme.description, None)
        self.assertEqual(
            theme.get_absolute_url(), "/" + theme.channel.slug + "/" + theme.slug + "/")

        print(
            "   --->  test_Theme_null_attribut of ThemeTestCase : OK !")
    """
		test attributs when a theme have many attributs
	"""

    def test_Theme_with_attributs(self):
        theme = Theme.objects.get(title="Theme1")
        theme.description = "blabla"
        self.assertEqual(theme.description, 'blabla')

        print(
            "   --->  test_Theme_with_attributs of ThemeTestCase : OK !")

    """
        test delete object
    """

    def test_delete_object(self):
        Theme.objects.get(id=1).delete()
        self.assertEquals(Theme.objects.all().count(), 0)

        print(
            "   --->  test_delete_object of ThemeTestCase : OK !")

"""
	test the type
"""


@override_settings(
    MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'media'),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite',
        }
    },
    LANGUAGE_CODE='en'
)
class TypeTestCase(TestCase):

    def setUp(self):
        Type.objects.create(title="Type1", slug="blabla")

        print(" --->  SetUp of TypeTestCase : OK !")

    """
		test all attributs when a type have been save with the minimum of attributs
	"""

    def test_Type_null_attribut(self):
        type1 = Type.objects.annotate(video_count=Count(
            "pod", distinct=True)).get(title="Type1")
        self.assertFalse(type1.slug == slugify("blabla"))
        self.assertEqual(type1.headband, None)
        self.assertEqual(type1.__unicode__(), "Type1")
        self.assertEqual(type1.video_count, 0)
        self.assertEqual(type1.description, None)

        print(
            "   --->  test_Type_null_attribut of TypeTestCase : OK !")

    """
		test attributs when a type have many attributs
	"""

    def test_Type_with_attributs(self):
        type1 = Type.objects.get(title="Type1")
        type1.description = "blabla"
        self.assertEqual(type1.description, 'blabla')

        print(
            "   --->  test_Type_with_attributs of TypeTestCase : OK !")

    """
        test delete object
    """

    def test_delete_object(self):
        Type.objects.get(id=1).delete()
        self.assertEquals(Type.objects.all().count(), 0)

        print(
            "   --->  test_delete_object of TypeTestCase : OK !")


"""
	test the discipline
"""


@override_settings(
    MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'media'),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite',
        }
    },
    LANGUAGE_CODE='en'
)
class DisciplineTestCase(TestCase):

    def setUp(self):
        Discipline.objects.create(title="Discipline1", slug="blabla")

        print(" --->  SetUp of DisciplineTestCase : OK !")

    """
		test all attributs when a discipline have been save with the minimum of attributs
	"""

    def test_Discipline_null_attribut(self):
        discipline = Discipline.objects.annotate(
            video_count=Count("pod", distinct=True)).get(title="Discipline1")
        self.assertFalse(discipline.slug == slugify("blabla"))
        self.assertEqual(discipline.headband, None)
        self.assertEqual(discipline.__unicode__(), "Discipline1")
        self.assertEqual(discipline.video_count, 0)
        self.assertEqual(discipline.description, None)

        print(
            "   --->  test_Discipline_null_attribut of DisciplineTestCase : OK !")

    """
		test attributs when a discipline have many attributs
	"""

    def test_Discipline_with_attributs(self):
        discipline = Discipline.objects.get(title="Discipline1")
        discipline.description = "blabla"
        self.assertEqual(discipline.description, 'blabla')

        print(
            "   --->  test_Discipline_with_attributs of DisciplineTestCase : OK !")

    """
        test delete object
    """

    def test_delete_object(self):
        Discipline.objects.get(id=1).delete()
        self.assertEquals(Discipline.objects.all().count(), 0)

        print(
            "   --->  test_delete_object of DisciplineTestCase : OK !")


"""
	test the NextAutoIncrement
"""


@override_settings(
    MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'media'),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite',
        }
    },
    LANGUAGE_CODE='en'
)
class NextAutoIncrementTestCase(TestCase):

    def setUp(self):
        discipline = Discipline.objects.create(title="Discipline1")

        print(" --->  SetUp of NextAutoIncrementTestCase : OK !")

    """
		Verifie if the id is incremented
	"""

    def testAutoIncrementId(self):
        if('mysql' in settings.DATABASES['default']['ENGINE']):
            self.assertEqual(get_nextautoincrement(
                Discipline), Discipline.objects.get(title="Discipline1").id + 1)
        else:
            self.assertEqual(Discipline.objects.latest(
                'id').id + 1, Discipline.objects.get(title="Discipline1").id + 1)

            print(
                "   --->  testAutoIncrementId of NextAutoIncrementTestCase : OK !")

"""
	test the objet pod and Video
"""


@override_settings(
    MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'media'),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite',
        }
    },
    LANGUAGE_CODE='en'
)
class VideoTestCase(TestCase):
    fixtures = ['initial_data.json', ]

    def setUp(self):
        remi = User.objects.create_user("Remi")
        other_type = Type.objects.get(id=1)
        self.media_guard_hash = get_media_guard("remi", 1)
        Pod.objects.create(
            type=other_type, title="Video1", owner=remi, video="", to_encode=False)
        Pod.objects.create(type=other_type, title="Video2", encoding_status="b", encoding_in_progress=True,
                           date_added=datetime.today(), owner=remi, date_evt=datetime.today(), video=os.path.join("media", "videos", "remi", self.media_guard_hash, "test.mp4"), allow_downloading=True, view_count=2, description="fl",
                           overview="blabla.jpg", is_draft=False, duration=3, infoVideo="videotest", to_encode=False)
        print(" --->  SetUp of VideoTestCase : OK !")

    """
		test all attributs when a video have been save with the minimum of attributs
	"""

    def test_Video_null_attributs(self):
        pod = Pod.objects.get(id=1)
        self.assertEqual(pod.video.name, "")
        self.assertEqual(pod.allow_downloading, False)
        self.assertEqual(pod.description, '')
        self.assertFalse(pod.slug == slugify("tralala"))
        date = datetime.today()
        self.assertEqual(pod.owner, User.objects.get(username="Remi"))
        self.assertEqual(pod.date_added.year, date.year)
        self.assertEqual(pod.date_added.month, date.month)
        self.assertEqual(pod.date_added.day, date.day)
        self.assertEqual(pod.date_evt, pod.date_added)
        self.assertEqual(pod.view_count, 0)
        self.assertEqual(pod.is_draft, True)
        self.assertEqual(pod.to_encode, False)
        self.assertEqual(pod.encoding_status, None)
        self.assertEqual(pod.encoding_in_progress, False)
        self.assertEqual(pod.thumbnail, None)
        self.assertTrue(pod.to_encode == False)
        self.assertEqual(pod.duration, 0)
        self.assertEqual(pod.infoVideo, None)
        self.assertEqual(pod.get_absolute_url(), "/video/" + pod.slug + "/")
        self.assertEqual(pod.__unicode__(), "%s - %s" %
                         ('%04d' % pod.id, pod.title))  # pb unicode appel str

        print(
            "   --->  test_Video_null_attributs of VideoTestCase : OK !")

    """
		test attributs when a video have many attributs
	"""

    def test_Video_many_attributs(self):
        pod = Pod.objects.get(id=2)
        self.assertEqual(pod.video.name, os.path.join(
            'media', 'videos', 'remi', self.media_guard_hash, 'test.mp4'))
        self.assertEqual(pod.allow_downloading, True)
        self.assertEqual(pod.description, 'fl')
        self.assertEqual(pod.overview.name, "blabla.jpg")
        self.assertEqual(pod.view_count, 2)
        self.assertEqual(pod.allow_downloading, True)
        self.assertEqual(pod.encoding_status, 'b')
        self.assertEqual(pod.to_encode, False)
        self.assertEqual(pod.is_draft, False)
        self.assertEqual(pod.encoding_in_progress, True)
        self.assertEqual(pod.duration, 3)
        self.assertEqual(pod.infoVideo, "videotest")
        self.assertEqual(pod.video.__unicode__(), pod.video.name)

        print(
            "   --->  test_Video_many_attributs of VideoTestCase : OK !")

    """
		test the function admin thumbnail
	"""

    def test_admin_thumbnail(self):
        video1 = Pod.objects.get(id=1)
        video2 = Pod.objects.get(id=2)
        self.assertEqual(video1.admin_thumbnail(), "")
        self.assertEqual(video2.admin_thumbnail(), "")  # test dans la vue

        print(
            "   --->  test_admin_thumbnail of VideoTestCase : OK !")

    """
		test the filename function
	"""

    def test_filename(self):
        video1 = Pod.objects.get(id=1)
        video2 = Pod.objects.get(id=2)
        self.assertEqual(video1.filename(), "")
        self.assertEqual(video2.filename(), u'test.mp4')

        print(
            "   --->  test_filename of VideoTestCase : OK !")

    """
		test the fucntion duration_in_time
	"""

    def test_duration_in_time(self):
        video1 = Pod.objects.get(id=1)
        video2 = Pod.objects.get(id=2)
        self.assertEqual(video1.duration_in_time(), "00:00:00")
        self.assertEqual(video2.duration_in_time(), "00:00:03")

        print(
            "   --->  test_duration_in_time of VideoTestCase : OK !")

    """
        test delete object
    """

    def test_delete_object(self):
        Pod.objects.get(id=1).delete()
        Pod.objects.get(id=2).delete()
        self.assertEquals(Pod.objects.all().count(), 0)

        print(
            "   --->  test_delete_object of VideoTestCase : OK !")

        
"""
    test the contributor object
"""


@override_settings(
    MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'media'),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite',
        }
    },
    LANGUAGE_CODE='en'
)
class ContributorPodsTestCase(TestCase):
    fixtures = ['initial_data.json', ]
  
    def setUp(self):
        remi = User.objects.create_user("Remi")
        other_type = Type.objects.get(id=1)
        pod = Pod.objects.create(
            type=other_type, title="Video1", slug="tralala", owner=remi)
        pod2 = Pod.objects.create(
            type=other_type, title="Video2", slug="tralalo", owner=remi)
        ContributorPods.objects.create(video=pod, name="contributor1")
        ContributorPods.objects.create(video=pod, name="contributor2", email_address="test@mail.com", role="actor", weblink="http://test.com")

        print (" ---> SetUp of ContributorPodsTestCase : OK !")

    """
        test all attributs when a contributor have been save with the minimum of attributs
    """

    def test_Contributor_null_attribut(self):
        contributor = ContributorPods.objects.get(id=1)
        self.assertEqual(contributor.video.id, 1)
        self.assertEqual(contributor.name, "contributor1")
        self.assertEqual(contributor.email_address, "")
        self.assertEqual(contributor.role, "author")
        self.assertEqual(contributor.weblink, None)
        self.assertEqual(contributor.__unicode__(), "Video:%s - Name:%s - Role:%s" % 
                          (contributor.video, contributor.name, contributor.role))

        print (
            "   ---> test_Contributor_null_attribut of ContributorPodsTestCase : OK !")

    """
        test attributs when a contributor have many attributs
    """

    def test_Contributor_with_attributs(self):
        contributor = ContributorPods.objects.get(id=2)
        self.assertEqual(contributor.email_address, "test@mail.com")
        self.assertEqual(contributor.role, "actor")
        self.assertEqual(contributor.weblink, "http://test.com")

        print (
            "   ---> test_Contributor_with_attributs of ContributorPodsTestCase : OK !")

    """
        test delete object
    """

    def test_delete_object(self):
        ContributorPods.objects.get(id=1).delete()
        ContributorPods.objects.get(id=2).delete()
        self.assertEquals(ContributorPods.objects.all().count(), 0)

        print (
            "   ---> test_delete_object of ContributorPodsTestCase : OK !")

"""
    test the trackpods object
"""


@override_settings(
    MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'media'),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite',
        }
    },
    LANGUAGE_CODE='en'
)
class TrackPodsTestCase(TestCase):
    fixtures = ['initial_data.json', ]

    def setUp(self):
        remi = User.objects.create_user("Remi")
        other_type = Type.objects.get(id=1)
        pod = Pod.objects.create(
            type=other_type, title="Video1", slug="tralala", owner=remi)
        pod2 = Pod.objects.create(
            type=other_type, title="Video2", slug="tralalo", owner=remi)
        TrackPods.objects.create(video=pod, lang="en")
        TrackPods.objects.create(video=pod2, lang="fr", kind="captions")

    """
        test all attributs when a track have been save with the minimum of attributs
    """

    def test_Track_null_attribut(self):
        track = TrackPods.objects.get(id=1)
        self.assertEqual(track.video.id, 1)
        self.assertEqual(track.lang, "en")
        self.assertEqual(track.kind, "subtitles")
        self.assertEqual(track.src, None)
        self.assertEqual(track.__unicode__(), "%s - File: %s - Video: %s" % 
                          (track.kind, track.src, track.video))

        print (
            "   ---> test_Track_null_attribut of TrackPodsTestCase : OK !")

    """
        test attributs when a track have many attributs
    """

    def test_Track_with_attributs(self):
        track = TrackPods.objects.get(id=2)
        self.assertEqual(track.lang, "fr")
        self.assertEqual(track.kind, "captions")

        print (
            "   ---> test_Track_with_attributs of TrackPodsTestCase : OK !")

    """
        test delete object
    """

    def test_delete_object(self):
        TrackPods.objects.get(id=1).delete()
        TrackPods.objects.get(id=2).delete()
        self.assertEquals(TrackPods.objects.all().count(), 0)

        print (
            "   ---> test_delete_object of TrackPodsTestCase : OK !")


"""
    test the chapter object
"""


@override_settings(
    MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'media'),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite',
        }
    },
    LANGUAGE_CODE='en'
)
class ChapterPodsTestCase(TestCase):
    fixtures = ['initial_data.json', ]

    def setUp(self):
        remi = User.objects.create_user("Remi")
        other_type = Type.objects.get(id=1)
        pod = Pod.objects.create(
            type=other_type, title="Video1", slug="tralala", owner=remi)
        ChapterPods.objects.create(video=pod, title="chapter1")
        ChapterPods.objects.create(video=pod, title="chapter2", time=2)

    """
        test all attributs when a chapter have been save with the minimum of attributs
    """

    def test_Chapter_null_attribut(self):
        chapter = ChapterPods.objects.get(id=1)
        self.assertEqual(chapter.video.id, 1)
        self.assertEqual(chapter.title, "chapter1")
        self.assertEqual(chapter.time, 0)
        self.assertFalse(chapter.slug == slugify("chapter1"))
        self.assertEqual(chapter.__unicode__(), "Chapter : %s - video: %s" % 
                          (chapter.title, chapter.video))

        print (
            "   ---> test_Chapter_null_attribut of ChapterPodsTestCase : OK !")

    """
        test attributs when a chapter have many attributs
    """

    def test_Chapter_with_attributs(self):
        chapter = ChapterPods.objects.get(id=2)
        self.assertEqual(chapter.title, "chapter2")
        self.assertEqual(chapter.time, 2)

        print (
            "   ---> test_Chapter_with_attributs of ChapterPodsTestCase : OK !")



    """
        test delete object
    """

    def test_delete_object(self):
        ChapterPods.objects.get(id=1).delete()
        ChapterPods.objects.get(id=2).delete()
        self.assertEquals(ChapterPods.objects.all().count(), 0)

        print (
            "   ---> test_delete_object of ChapterPodsTestCase : OK !")
        

"""
    test the overlaypods object
"""



@override_settings(
    MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'media'),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite',
        }
    },
    LANGUAGE_CODE='en'
)
class OverlayPodsTestCase(TestCase):
    fixtures = ['initial_data.json', ]

    def setUp(self):
        remi = User.objects.create_user("Remi")
        other_type = Type.objects.get(id=1)
        pod = Pod.objects.create(
            type=other_type, title="Video1", slug="tralala", owner=remi)
        OverlayPods.objects.create(
            video=pod, title="overlay1", content="tralala")
        OverlayPods.objects.create(
            video=pod, title="overlay2", content="tralala", time_end=5, position="top-left")

        print(" ---> SetUp of OverlayPodsTestCase : OK !")

    """
        test atributs and str function
    """

    def test_attributs_and_str(self):
        overlay = OverlayPods.objects.get(id=1)
        overlay2 = OverlayPods.objects.get(id=2)
        self.assertEqual(overlay.video.id, 1)
        self.assertEqual(overlay.content, "tralala")
        self.assertEqual(overlay.time_start, 0)
        self.assertEqual(overlay.time_end, 1)
        self.assertEqual(overlay.position, "bottom-right")
        self.assertEqual(overlay2.time_end, 5)
        self.assertEqual(overlay2.position, "top-left")
        self.assertEqual(overlay.__unicode__(), "Overlay : %s - video: %s" %
                         (overlay.title, overlay.video))

        print(
            "   ---> test_attributs_and_str of OverlayPodsTestCase : OK !")
        
    def test_delete_object(self):
        OverlayPods.objects.get(id=1).delete()
        OverlayPods.objects.get(id=2).delete()
        self.assertEquals(OverlayPods.objects.all().count(), 0)

        print(
            "   ---> test_delete_object of OverlayPodsTestCase : OK !")


"""
	test the favorites object
"""


@override_settings(
    MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'media'),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite',
        }
    },
    LANGUAGE_CODE='en'
)
class FavoritesTestCase(TestCase):
    fixtures = ['initial_data.json', ]

    def setUp(self):
        remi = User.objects.create_user("Remi")
        other_type = Type.objects.get(id=1)
        pod = Pod.objects.create(
            type=other_type,  title="Video1", slug="tralala", owner=remi)
        Favorites.objects.create(user=remi, video=pod)

        print(" --->  SetUp of FavoritesTestCase : OK !")

    """
		test attributs and str function
	"""

    def test_attributs_and_str(self):
        favorite = Favorites.objects.get(id=1)
        self.assertEqual(favorite.user.username, "Remi")
        self.assertEqual(favorite.video.id, 1)
        self.assertEqual(favorite.__unicode__(), "%s-%s" %
                         (favorite.user.username, favorite.video))

        print(
            "   --->  test_attributs_and_str of FavoritesTestCase : OK !")
    """
        test delete object
    """

    def test_delete_object(self):
        Favorites.objects.get(id=1).delete()
        self.assertEquals(Favorites.objects.all().count(), 0)

        print(
            "   --->  test_delete_object of FavoritesTestCase : OK !")


"""
	test the objet Notes
"""


@override_settings(
    MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'media'),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite',
        }
    },
    LANGUAGE_CODE='en'
)
class NotesTestCase(TestCase):
    fixtures = ['initial_data.json', ]

    def setUp(self):
        remi = User.objects.create_user("Remi")
        other_type = Type.objects.get(id=1)
        pod = Pod.objects.create(
            type=other_type,  title="Video1", slug="tralala", owner=remi)
        pod2 = Pod.objects.create(
            type=other_type,  title="Video2", slug="tralala", owner=remi)
        Notes.objects.create(user=remi, video=pod, note="tata")
        Notes.objects.create(user=remi, video=pod2)

        print(" --->  SetUp of NotesTestCase : OK !")

    """
		test attributs and str function
	"""

    def test_attributs_and_str(self):
        note = Notes.objects.get(id=1)
        note2 = Notes.objects.get(id=2)
        self.assertEqual(note.user.username, "Remi")
        self.assertEqual(note.video.id, 1)
        self.assertEqual(note.note, "tata")
        self.assertEqual(note2.note, None)
        self.assertEqual(note.__unicode__(), "%s-%s" %
                         (note.user.username, note.video))

        print(
            "   --->  test_attributs_and_str of NotesTestCase : OK !")

    """
        test delete object
    """

    def test_delete_object(self):
        Notes.objects.get(id=1).delete()
        Notes.objects.get(id=2).delete()
        self.assertEquals(Notes.objects.all().count(), 0)

        print(
            "   --->  test_delete_object of NotesTestCase : OK !")


@override_settings(
    MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'media'),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite',
        }
    },
    LANGUAGE_CODE='en'
)
class PlaylistTestCase(TestCase):
    fixtures = ['initial_data.json', ]

    def setUp(self):
        remi = User.objects.create_user("Remi")
        Playlist.objects.create(title='test1', owner=remi)
        Playlist.objects.create(title='test2', owner=remi, description='test', visible=True)
        print(" ----> SetUp of PlaylistTestCase : OK !")

    """
        test all attributs when a playlist have been save with the minimum of attributs
    """
    def test_Playlist_null_attributs(self):
        playlist = Playlist.objects.get(id=1)
        remi = User.objects.get(id=1)
        self.assertEqual(playlist.title, 'test1')
        self.assertEqual(playlist.slug, slugify('test1'))
        self.assertEqual(playlist.description, '')
        self.assertEqual(playlist.visible, False)
        self.assertEqual(playlist.owner, remi)
        print(
            "   ----> test_Playlist_null_attributs of PlaylistTestCase : OK !")

    """
        test all attributs when a playlist have many attributs
    """
    def test_Playlist_with_attributs(self):
        playlist = Playlist.objects.get(id=2)
        remi = User.objects.get(id=1)
        self.assertEqual(playlist.title, 'test2')
        self.assertEqual(playlist.slug, slugify('test2'))
        self.assertEqual(playlist.description, 'test')
        self.assertEqual(playlist.visible, True)
        self.assertEqual(playlist.owner, remi)
        print(
            "   ----> test_Playlist_with_attributs of PlaylistTestCase : OK !")

    """
        test delete object
    """
    def test_delete_object(self):
        Playlist.objects.get(id=1).delete()
        self.assertEqual(Playlist.objects.all().count(), 1)
        Playlist.objects.get(id=2).delete()
        self.assertEqual(Playlist.objects.all().count(), 0)
        print(
            "   ----> test_delete_object of PlaylistTestCase : OK !")


@override_settings(
    MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'media'),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite',
        }
    },
    LANGUAGE_CODE='en'
)
class PlaylistVideoTestCase(TestCase):
    fixtures = ['initial_data.json', ]

    def setUp(self):
        remi = User.objects.create_user("Remi")
        playlist = Playlist.objects.create(title='test1', owner=remi)
        other_type = Type.objects.get(id=1)
        pod = Pod.objects.create(
            type=other_type,  title="Video1", slug="tralala", owner=remi)
        pod2 = Pod.objects.create(
            type=other_type, title="Video2", slug="tralala2", owner=remi)
        PlaylistVideo.objects.create(playlist=playlist, video=pod)
        PlaylistVideo.objects.create(playlist=playlist, video=pod2, position=1)
        print(" ----> setUp of PlaylistVideoTestCase : OK !")

    def test_attributs(self):
        pod = Pod.objects.get(id=1)
        pod2 = Pod.objects.get(id=2)
        video = PlaylistVideo.objects.get(id=1)
        video2 = PlaylistVideo.objects.get(id=2)
        playlist = Playlist.objects.get(id=1)
        self.assertEqual(video.playlist, playlist)
        self.assertEqual(video.video, pod)
        self.assertEqual(video.position, 0)
        self.assertEqual(video2.playlist, playlist)
        self.assertEqual(video2.video, pod2)
        self.assertEqual(video2.position, 1)
        print(
            "   ----> test_attributs of PlaylistVideoTestCase : OK !")

    """
        test delete object
    """
    def test_delete_object(self):
        playlist = Playlist.objects.get(id=1)
        PlaylistVideo.objects.get(id=1).delete()
        self.assertEqual(PlaylistVideo.objects.all().count(), 1)
        video = PlaylistVideo.objects.get(id=2)
        video.reordering(playlist)
        self.assertEqual(PlaylistVideo.objects.get(id=2).position, 0)
        PlaylistVideo.objects.get(id=2).delete()
        self.assertEqual(PlaylistVideo.objects.all().count(), 0)
        print(
            "   ----> test_delete_object of PlaylistVideoTestCase : OK !")


"""
	test the MediaCourses
"""


@override_settings(
    MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'media'),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite',
        }
    },
    LANGUAGE_CODE='en'
)
class MediaCoursesTestCase(TestCase):
    fixtures = ['initial_data.json', ]

    def setUp(self):
        remi = User.objects.create_user("Remi")
        remi2 = User.objects.create_user("Remi2")
        Mediacourses.objects.create(user=remi, title="media1", date_added=timezone.now(
        ), mediapath="blabla", started=True, error="error1")
        #Mediacourses.objects.get_or_create(user=remi2, title="media2")
        Mediacourses.objects.create(user=remi2, title="media2", started=True)
        print(" --->  SetUp of MediaCoursesTestCase : OK !")

    """
		test attributs
	"""

    def test_attributs(self):
        media = Mediacourses.objects.get(id=1)
        media2 = Mediacourses.objects.get(id=2)
        # test media
        self.assertEqual(media.user.username, "Remi")
        self.assertEqual(media.title, "media1")
        date = datetime.today()
        self.assertEqual(media.date_added.year, date.year)
        self.assertEqual(media.date_added.month, date.month)
        self.assertEqual(media.date_added.day, date.day)
        self.assertEqual(media.mediapath, "blabla")
        self.assertEqual(media.started, True)
        self.assertEqual(media.error, "error1")
        # test media2
        self.assertEqual(media2.date_added.strftime(
            "%d/%m/%y"), media.date_added.strftime("%d/%m/%y"))
        self.assertEqual(media2.title, "media2")
        self.assertEqual(media2.started, True)
        self.assertEqual(media2.error, None)

        print(
            "   --->  test_attributs of MediaCoursesTestCase : OK !")

    """
        test delete object
    """

    def test_delete_object(self):
        Mediacourses.objects.filter(title="media1").delete()
        self.assertEquals(Mediacourses.objects.all().count(), 1)

        print(
            "   --->  test_delete_object of MediaCoursesTestCase : OK !")


"""
	test building object
"""


@override_settings(
    MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'media'),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite',
        }
    },
    LANGUAGE_CODE='en'
)
class BuildingTestCase(TestCase):

    def setUp(self):
        building = Building.objects.create(name="bulding1")

        print(" --->  SetUp of BuildingTestCase : OK !")

    """
		test attributs
	"""

    def test_attributs(self):
        building = Building.objects.get(id=1)
        self.assertEqual(building.name, u"bulding1")

        print(
            "   --->  test_attributs of BuildingTestCase : OK !")

    """
        test delete object
    """

    def test_delete_object(self):
        Building.objects.get(id=1).delete()
        self.assertEquals(Building.objects.all().count(), 0)

        print(
            "   --->  test_delete_object of BuildingTestCase : OK !")

"""
	test recorder object
"""


@override_settings(
    MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'media'),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite',
        }
    },
    LANGUAGE_CODE='en'
)
class RecoderTestCase(TestCase):
    fixtures = ['initial_data.json', ]

    def setUp(self):
        remi = User.objects.create_user("Remi")
        building = Building.objects.create(name="bulding1")
        image = Image.objects.create(owner=remi, original_filename="schema_bdd.jpg", file=File(
            open("schema_bdd.jpg"), "schema_bdd.jpg"))
        Recorder.objects.create(name="recorder1", image=image, adress_ip="201.10.20.10",
                                status=True, slide=False, gmapurl="b", is_restricted=True, building=building)

        print(" --->  SetUp of RecoderTestCase : OK !")

    """
		test attributs
	"""

    def test_attributs(self):
        record = Recorder.objects.get(id=1)
        self.assertEqual(record.name, "recorder1")
        self.assertEqual(record.image.original_filename, "schema_bdd.jpg")
        self.assertEqual(record.adress_ip, "201.10.20.10")
        self.assertEqual(record.status, True)
        self.assertEqual(record.slide, False)
        self.assertEqual(record.gmapurl, "b")
        self.assertEqual(record.is_restricted, True)
        self.assertEqual(record.building.id, 1)
        self.assertEqual(record.__unicode__(), "%s - %s" %
                         (record.name, record.adress_ip))
        self.assertEqual(record.ipunder(), "201_10_20_10")

        print(
            "   --->  test_attributs of RecoderTestCase : OK !")

    """
        test delete object
    """

    def test_delete_object(self):
        Recorder.objects.get(id=1).delete()
        self.assertEquals(Recorder.objects.all().count(), 0)

        print(
            "   --->  test_delete_object of RecoderTestCase : OK !")

"""
    test reportVideo object
"""


@override_settings(
    MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'media'),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite',
        }
    },
    LANGUAGE_CODE='en'
)
class ReportVideoTestCase(TestCase):
    fixtures = ['initial_data.json', ]

    def setUp(self):
        remi = User.objects.create_user("Remi")
        nicolas = User.objects.create_user("Nicolas")
        other_type = Type.objects.get(id=1)
        pod = Pod.objects.create(
            type=other_type,  title="Video1", slug="tralala", owner=remi)

        ReportVideo.objects.create(video=pod, user=remi)

        ReportVideo.objects.create(
            video=pod, user=nicolas, comment="violation des droits", answer="accepte")

        print(" --->  SetUp of ReportVideoTestCase : OK !")

    """
        test_attributs_with_not_comment
    """

    def test_attributs_with_not_comment(self):
        reportVideo = ReportVideo.objects.get(id=1)
        self.assertEqual(reportVideo.video.id, 1)
        self.assertEqual(reportVideo.__unicode__(), "%s - %s" %
                         (reportVideo.video, reportVideo.user))
        self.assertEqual(reportVideo.user.username, "Remi")
        date = datetime.today()
        self.assertEqual(reportVideo.date_added.year, date.year)
        self.assertEqual(reportVideo.date_added.month, date.month)
        self.assertEqual(reportVideo.date_added.day, date.day)
        self.assertEqual(reportVideo.comment, None)
        self.assertEqual(reportVideo.answer, None)
        yesterday = datetime.today() - timedelta(1)
        reportVideo.date = yesterday
        self.assertFalse(reportVideo.date_added.day == yesterday.day)

        print(
            "   --->  test_attributs_with_not_comment of ReportVideoTestCase : OK !")

    """
        test_attributs_with_comment
    """

    def test_attributs_with_comment(self):
        reportVideo = ReportVideo.objects.get(id=2)
        self.assertEqual(reportVideo.video.id, 1)
        self.assertEqual(reportVideo.__unicode__(), "%s - %s" %
                         (reportVideo.video, reportVideo.user))
        self.assertEqual(reportVideo.user.username, "Nicolas")
        date = datetime.today()
        self.assertEqual(reportVideo.date_added.year, date.year)
        self.assertEqual(reportVideo.date_added.month, date.month)
        self.assertEqual(reportVideo.date_added.day, date.day)
        self.assertEqual(reportVideo.comment, "violation des droits")
        self.assertEqual(reportVideo.answer, "accepte")
        self.assertEqual(reportVideo.get_iframe_url_to_video(),
                         reportVideo.video.get_iframe_admin_integration())

        print(
            "   --->  test_attributs_with_comment of ReportVideoTestCase : OK !")

    """
        test delete object
    """

    def test_delete_object(self):
        ReportVideo.objects.get(id=1).delete()
        ReportVideo.objects.get(id=2).delete()
        self.assertEquals(ReportVideo.objects.all().count(), 0)

        print(
            "   ---> test_delete_object of ReportVideoTestCase : OK !")


"""
    test the rss
"""


@override_settings(
    MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'media'),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite',
        }
    }
)
class RSSTestCase(TestCase):
    fixtures = ['initial_data.json', ]

    def setUp(self):
        if RSS:
            user = User.objects.create(
                username='remi', password='12345', is_active=True, is_staff=True)
            other_type = Type.objects.get(id=1)
            Rssfeed.objects.create(title='test1', description="blabla",
                                   link_rss='http://test.com', owner=user, fil_type_pod=other_type)
            Rssfeed.objects.create(title='test2', description="blabla",
                                   link_rss='http://test.com', owner=user, fil_type_pod=other_type, type_rss='V', year=2018, is_up=False)

            print(" ---> SetUp of RSSTestCase : OK !")

    """
        test all attributs when a rssfeed have been save with the minimum of attributs
    """

    def test_Rssfeed_null_attribut(self):
        if RSS:
            date = datetime.today()
            user = User.objects.get(username='remi')
            rssfeed = Rssfeed.objects.get(id=1)
            self.assertEqual(rssfeed.title, 'test1')
            self.assertEqual(rssfeed.year, 2017)
            self.assertEqual(rssfeed.type_rss, 'A')
            self.assertEqual(rssfeed.is_up, True)
            self.assertEqual(rssfeed.limit, 0)
            self.assertEqual(rssfeed.date_update.year, date.year)
            self.assertEqual(rssfeed.date_update.month, date.month)
            self.assertEqual(rssfeed.date_update.day, date.day)
            self.assertEqual(rssfeed.owner, user)
            self.assertEqual(rssfeed.__unicode__(), rssfeed.title)

            print(
                "   ---> test_Rssfeed_null_attribut of RSSTestCase : OK !")

    """
        test attributs when a rssfeed have many attributs
    """

    def test_Rssfeed_with_attributs(self):
        if RSS:
            date = datetime.today()
            user = User.objects.get(username='remi')
            rssfeed = Rssfeed.objects.get(id=2)
            self.assertEqual(rssfeed.year, 2018)
            self.assertEqual(rssfeed.type_rss, 'V')
            self.assertEqual(rssfeed.is_up, False)
            self.assertEqual(rssfeed.limit, 0)
            self.assertEqual(rssfeed.date_update.year, date.year)
            self.assertEqual(rssfeed.date_update.month, date.month)
            self.assertEqual(rssfeed.date_update.day, date.day)
            self.assertEqual(rssfeed.owner, user)
            self.assertEqual(rssfeed.__unicode__(), rssfeed.title)

            print(
                "   ---> test_Rssfeed_with_attributs of RSSTestCase : OK !")

    """
        test delete object
    """

    def test_delete_object(self):
        if RSS:
            Rssfeed.objects.get(id=1).delete()
            Rssfeed.objects.get(id=2).delete()
            self.assertEquals(Rssfeed.objects.all().count(), 0)

            print(
                "   ---> test_delete_object of RSSTestCase : OK !")
