import Vue from 'vue';
import Router from 'vue-router';
import LoginPage from './components/LoginPage.vue';
import HomePage from './components/HomePage.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    { path: '/', component: LoginPage },
    { path: '/user', component: HomePage }
  ]
});