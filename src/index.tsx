import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import Header from './component/Header/Header'
import Post from './component/Post/Post'
import Login from './component/Login/index'
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>
    {/* <Login/> */}
    <Header/>
    <Post/>
    
    
    
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();