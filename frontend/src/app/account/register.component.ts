import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { CustomValidators } from '../custom-validators';
import { MustMatch } from '@app/_helpers/must-match.validator';

@Component({ 
    selector: 'app-root',
    templateUrl: 'register.component.html' 
})

export class RegisterComponent implements OnInit {
    fieldTextType: boolean;
    repeatFieldTextType: boolean;
    loading = false;
    submitted = false;
    public regform: FormGroup;
    
    constructor(
        private readonly http: HttpClient,
        private formBuilder: FormBuilder,
        private router: Router,
    ) 
    {
      this.regform = this.createSignupForm();    
    }

    createSignupForm(): FormGroup {
      return this.formBuilder.group(
        {
          firstName: [
            null,
            Validators.compose([ Validators.required,
              CustomValidators.patternValidator(/^[A-Za-z]+$/, {
                hasCapitalCase: true
              })
             ])
          ],
          lastName: [
                null,
                Validators.compose([Validators.required,
                  CustomValidators.patternValidator(/^[A-Za-z]+$/, {
                    hasCapitalCase: true
                  })])
              ],
          email: [
            '',
            Validators.compose([Validators.email, Validators.required, 
              Validators.pattern("^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$")]),
          ],
          password: [
            null,
            Validators.compose([
              Validators.required,
              // check whether the entered password has a number
              CustomValidators.patternValidator(/\d/, {
                hasNumber: true
              }),
              // check whether the entered password has upper case letter
              CustomValidators.patternValidator(/[A-Z]/, {
                hasCapitalCase: true
              }),
              // check whether the entered password has a lower case letter
              CustomValidators.patternValidator(/[a-z]/, {
                hasSmallCase: true
              }),
              // check whether the entered password has a special character
              CustomValidators.patternValidator(
                /[ !@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/,
                {
                  hasSpecialCharacters: true
                }
              ),
              Validators.minLength(8)
            ])
          ],
          confirmPassword: ['', Validators.required]
         },
          {
        validator: MustMatch('password', 'confirmPassword')
           }
      );
  
     
    }
  ngOnInit() {}

    // convenience getter for easy access to form fields
    get f() { return this.regform.controls; }

    public onSubmit():void  {
        console.log(this.regform.value); 
        var val=this.regform.value;
        this.http.post('http://localhost:5000/register_data/ ', val).subscribe((response)=>{
            let value =response["response"]; 
            if (value == true){
                console.log(value)
                this.router.navigate(['/account/login']); 
            }else{
                console.log(value)
                this.router.navigate(['/account/register']); 
            }
          });
    }

    toggleFieldTextType() {
      this.fieldTextType = !this.fieldTextType;
    }
  
    toggleRepeatFieldTextType() {
      this.repeatFieldTextType = !this.repeatFieldTextType;
    }
}