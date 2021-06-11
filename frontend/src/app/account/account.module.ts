import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { AccountRoutingModule } from './account-routing.module';
import { LayoutComponent } from './layout.component';
import { LoginComponent } from './login.component';
import { RegisterComponent } from './register.component';
import { VerifyEmailComponent } from './verify-email.component';
import { ForgotPasswordComponent } from './forgot-password.component';
import { ResetPasswordComponent } from './reset-password.component';
import { OtpComponent } from './otp.component';
import { WelcomeComponent } from './welcome.component';
import { AccessGuard } from './account-routing.module';





@NgModule({
    imports: [
        CommonModule,
        ReactiveFormsModule,
        AccountRoutingModule,
        FormsModule,
        ReactiveFormsModule

    ],
    declarations: [
        LayoutComponent,
        LoginComponent,
        RegisterComponent,
        VerifyEmailComponent,
        ForgotPasswordComponent,
        ResetPasswordComponent,
        OtpComponent,
        WelcomeComponent
        ],
        providers:[
            AccessGuard,
            LoginComponent
                ]
})
export class AccountModule { }