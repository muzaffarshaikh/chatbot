import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { UnavailableComponent } from './unavailable/unavailable.component'
const accountModule = () => import('./account/account.module').then(x => x.AccountModule);
import { WelcomeComponent } from './account/welcome.component';



const routes: Routes = [
    { path: 'account', loadChildren: accountModule },
    { path: '', redirectTo: 'home', pathMatch:'full'},
    { path: 'home', component: WelcomeComponent },
    { path: '404', component: UnavailableComponent },
    { path: '**', component: UnavailableComponent },
];

@NgModule({
    imports: [RouterModule.forRoot(routes, { relativeLinkResolution: 'legacy' })],
    exports: [RouterModule]
})
export class AppRoutingModule { }
