import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormBuilder,FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';


declare const chat: any;
declare const diable_back_button:any;

@Component({ 
    selector: 'app-root',
    templateUrl: 'login.component.html' 
})


export class LoginComponent implements OnInit {
    logform: FormGroup;
    loading = false;
    submitted = false;
    fieldTextType: boolean;
    message: string;

    constructor(
        private readonly http: HttpClient,
        private formBuilder: FormBuilder,
        private router: Router,
    ) 
    {
      this.logform = this.createLoginForm();
    }
    createLoginForm(): FormGroup {
        return this.formBuilder.group(
          {
            email: [
                '',
                Validators.compose([Validators.email, Validators.required, 
                  Validators.pattern("^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$")]),
                ],
                password: [
                  null,
                  Validators.compose([
                    Validators.required
                  ])
                ]
          }
        );
    }
    ngOnInit() {
    }

    get f() { return this.logform.controls; }
     
    public onSubmit():void  {
        this.http.get('http://localhost:5000/validation/ ').subscribe((response)=>{
            let message = response["response"];
                console.log(message)
             });
        }

    public subject = new Subject<string>();
    public subject1 = new Subject<boolean>();

      log1(): Observable<string> {
        var val=this.logform.value;
        this.http.post('http://localhost:5000/login_data/ ', val).subscribe(
         (response)=>
     {  
          let b = response["response"]; 
          if(b == true){
            this.router.navigate(['/account/chatbot']);
            this.subject.next('trueeeeeeeee!!');
            return this.subject.next('TRUE');
          }
            else{
              this.message='Invalid Usernam/Password !'
              console.log("You are not logged in",this.subject)
              this.subject.next("FALSE");
            }  
          }
        );
       return this.subject.asObservable();
        }

        log2(): Observable<boolean>|Promise<boolean>|boolean {
          this.http.get('http://localhost:5000/logged_user/ ').subscribe(
           (response)=>
       {  
            let b = response["response"]; 
            if(b == true){
              console.log("You are now logged in")
              this.subject1.next(true);
              return this.subject1.next(true);
            }
              else{
                console.log("You are not logged in")
                this.subject1.next(false);
              }  
            }
          );
            return this.subject1.asObservable();
          }

          toggleFieldTextType() {
            this.fieldTextType = !this.fieldTextType;
          }
  
}









