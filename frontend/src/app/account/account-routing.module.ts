import { Injectable, NgModule } from '@angular/core';
import { Routes, RouterModule, ActivatedRouteSnapshot, CanActivate, Router } from '@angular/router';
import { LayoutComponent } from './layout.component';
import { LoginComponent } from './login.component';
import { RegisterComponent } from './register.component';
import { VerifyEmailComponent } from './verify-email.component';
import { ForgotPasswordComponent } from './forgot-password.component';
import { ResetPasswordComponent } from './reset-password.component';
import { OtpComponent} from './otp.component';
import {  ChatbotComponent } from '../chatbot/chatbot.component';
import { UnavailableComponent } from '../unavailable/unavailable.component'
import { Observable } from 'rxjs';
import { WelcomeComponent } from './welcome.component';

@Injectable()
export class AccessGuard implements CanActivate {   
constructor( private logcomp:LoginComponent){}

  canActivate(route: ActivatedRouteSnapshot): Observable<boolean>|Promise<boolean>|boolean {
    const requiresLogin = route.data.requiresLogin || false;   
    if (requiresLogin) {
        if(this.logcomp.log2() == true){
            return true;
        }
       else{
        return this.logcomp.log2()
       }
    }
  }
}


const routes: Routes = [
    {
        path: '', component: LayoutComponent,
        children: [
            { path: '', redirectTo: 'home', pathMatch:'full'},
            { path: 'home', component: WelcomeComponent },
            { path: 'welcome', component: WelcomeComponent},
            { path: 'login', component: LoginComponent},
            { path: 'register', component: RegisterComponent },
            { path: 'verify-email', component: VerifyEmailComponent },
            { path: 'forgot-password', component: ForgotPasswordComponent },
            { path: 'reset-password', component: ResetPasswordComponent },
            { path: 'otp', component: OtpComponent },
            { path: 'chatbot', component: ChatbotComponent,data:{requiresLogin: true},canActivate: [ AccessGuard ]},
            { path: '404', component: UnavailableComponent },
            { path: '**', component: UnavailableComponent }
        ]
    }
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class AccountRoutingModule { }
