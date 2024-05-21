import { createRouter, createWebHashHistory } from 'vue-router'
import ContainVideosView from '@/views/ContainVideosView.vue'
import PlayerView from '../views/PlayerView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import NotFoundView from '../views/404NotFoundView.vue'
import HomeView from '../views/HomeView.vue'
import UserProfileView from '@/views/UserProfileView.vue'
import MyVideosView from '@/views/MyVideosView.vue'
import DailyListenView from '../views/DailyListenView.vue'
import ForeignListenView from '../views/ForeignListenView.vue'
import PastPapersView from '../views/PastPapersView.vue'
import QualityListenView from '../views/QualityListenView.vue'
import NoteBookView from '../views/NoteBookView.vue'
import NeighborhoodView from '../views/NeighborhoodView.vue'
import CloudFileView from '../views/CloudFileView.vue'

const routes = [{
        path: '',
        name: 'home',
        component: HomeView,
    },
    {
        path: '/',
        name: 'home',
        component: HomeView,
    }, {
        path: '/home/',
        name: 'home',
        component: HomeView,
    }, {
        path: '/listen/',
        name: 'ContainVideos',
        component: ContainVideosView
    }, {
        path: '/player/',
        name: 'player',
        component: PlayerView,
    }, {
        path: '/login/',
        name: 'login',
        component: LoginView,
    }, {
        path: '/register/',
        name: 'register',
        component: RegisterView,
    }, {
        path: '/userprofile/:userId/',
        name: 'userprofile',
        component: UserProfileView,
    }, {
        path: '/myvideos/',
        name: "myvideos",
        component: MyVideosView,
    }, {
        path: '/dailylisten/',
        name: "dailyListen",
        component: DailyListenView,
    }, {
        path: '/foreignlisten/',
        name: "foreignListen",
        component: ForeignListenView,
    }, {
        path: '/pastPapers/',
        name: "pastPapers",
        component: PastPapersView,
    }, {
        path: '/notebooks/',
        name: "notebooks",
        component: NoteBookView,
    }, {
        path: '/qualityListen/',
        name: 'qualityListen',
        component: QualityListenView,
    }, {
        path: '/neighborhood/',
        name: 'neighborhood',
        component: NeighborhoodView,
    }, {
        path: '/cloudfile/',
        name: 'cloudfile',
        component: CloudFileView,
    }, {
        path: '/:catchAll(.*)/',
        name: '404',
        component: NotFoundView,
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router