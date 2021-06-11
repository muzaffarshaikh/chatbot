import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MustMatch } from '@app/_helpers/must-match.validator';

@Component({
    selector: 'app-root',
     templateUrl: './reset-password.component.html',
     styleUrls: []
     })

export class ResetPasswordComponent {
    fieldTextType: boolean;
    repeatFieldTextType: boolean;
    form: FormGroup;
    loading = false;
    submitted = false;

    public resetform: FormGroup;

    constructor(
        private formBuilder: FormBuilder,
     ) {}

    ngOnInit() {
        this.form = this.formBuilder.group({
            password: ['', [Validators.required, Validators.minLength(6)]],
            confirmPassword: ['', Validators.required],
        }, {
            validator: MustMatch('password', 'confirmPassword')
        });

        
      }
    
    get f() { return this.form.controls; }

    onSubmit() {
        
    }

    toggleFieldTextType() {
        this.fieldTextType = !this.fieldTextType;
      }
    
      toggleRepeatFieldTextType() {
        this.repeatFieldTextType = !this.repeatFieldTextType;
      }

  
}