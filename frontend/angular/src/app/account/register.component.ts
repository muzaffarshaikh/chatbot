import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';
import { HttpClient } from '@angular/common/http';
import { RestService } from '../rest.service';
import { AccountService, AlertService } from '@app/_services';
import { MustMatch } from '@app/_helpers';

@Component({ 
    selector: 'app-root',
    templateUrl: 'register.component.html' 
})
export class RegisterComponent implements OnInit {

    loading = false;
    submitted = false;
    url_for : RestService;

    public regform: FormGroup;
    
    constructor(
        private readonly http: HttpClient,
        public rs: RestService,
        private formBuilder: FormBuilder,
        private route: ActivatedRoute,
        private router: Router,
        private accountService: AccountService,
        private alertService: AlertService
    ) 
    {this.regform = new FormGroup({
        'firstName': new FormControl('', [
          Validators.required
        ]),
        'lastName': new FormControl('', [
          Validators.required
        ]),
        'email': new FormControl('', [
          Validators.required
        ]),
        'password': new FormControl('', [
          Validators.required
        ]),
        'confirmPassword': new FormControl('', [
          Validators.required
        ])
      }); }
     
  
        ngOnInit() {
        this.regform = this.formBuilder.group({
            title: ['', Validators.required],
            firstName: ['', Validators.required],
            lastName: ['', Validators.required],
            email: ['', [Validators.required, Validators.email]],
            password: ['', [Validators.required, Validators.minLength(6)]],
            confirmPassword: ['', Validators.required]
        }, {
            validator: MustMatch('password', 'confirmPassword')
        });
    }

    // convenience getter for easy access to form fields
    get f() { return this.regform.controls; }

    public onSubmit():void  {
        console.log(this.regform.value); // printing the values(user input) in console
        var val=this.regform.value;
        this.http.post("http://localhost:5000/register_data/ ", val).subscribe((data) => {});

        this.submitted = true;

        // reset alerts on submit
        this.alertService.clear();

        // stop here if form is invalid
        if (this.regform.invalid) {
            return;
        }

        this.loading = true;
        this.accountService.register(this.regform.value)
            .pipe(first())
            .subscribe({
                next: () => {
                    this.alertService.success('Registration successful, please check your email for verification instructions', { keepAfterRouteChange: true });
                    this.router.navigate(['../login'], { relativeTo: this.route });
                },
                error: error => {
                    this.alertService.error(error);
                    this.loading = false;
                }
            });
    }
}