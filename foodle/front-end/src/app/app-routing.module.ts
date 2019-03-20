import './polyfills';

import {HttpClientModule} from '@angular/common/http';
import {NgModule} from '@angular/core';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {MatNativeDateModule} from '@angular/material';
import {BrowserModule} from '@angular/platform-browser';
import {platformBrowserDynamic} from '@angular/platform-browser-dynamic';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import { CommonModule } from '@angular/common';

import {DemoMaterialModule} from './material-module';

import {TabComponent} from './tab/tab.component';
import { MatTabsModule } from '@angular/material';


@NgModule({
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    FormsModule,
    HttpClientModule,
    MatTabsModule,
    DemoMaterialModule,
    MatNativeDateModule,
    ReactiveFormsModule,
    TabComponent,
    CommonModule
  ],
  entryComponents: [TabComponent],
  declarations: [TabComponent],
  bootstrap: [TabComponent],
  providers: []
})
export class AppRoutingModule { }


platformBrowserDynamic().bootstrapModule(AppRoutingModule);

