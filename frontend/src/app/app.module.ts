import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {  FormsModule,ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ChatbotComponent } from './chatbot/chatbot.component';
import { UnavailableComponent } from './unavailable/unavailable.component';
import { AccessGuard } from './account/account-routing.module';

@NgModule({
    imports: [
        BrowserModule,
        ReactiveFormsModule,
        FormsModule,
        HttpClientModule,
        AppRoutingModule
    ],
    declarations: [
        AppComponent,
        ChatbotComponent ,
        UnavailableComponent
    ],
    providers: [
       AccessGuard
    ],
    bootstrap: [AppComponent]
})
export class AppModule { }