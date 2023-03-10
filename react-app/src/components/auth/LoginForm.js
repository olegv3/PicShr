import { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Link, Redirect, useLocation } from 'react-router-dom';
import { login } from '../../store/session';
import './LoginForm.css';

const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();
  const location = useLocation();
  const prevLocation = location.search.split('=')[1];

  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  const handleLogin = async (event) => {
    event.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    }
  };

  const handleDemoUser = (event) => {
    event.preventDefault();
    const demoEmail = 'demo@aa.io';
    const demoPassword = 'password';
    dispatch(login(demoEmail, demoPassword));
  };

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  if (user) {
    return <Redirect to={prevLocation} />;
  }

  return (
    <div className="background-for-signup-and-login">
      <div className="whole-sign-up-container">
        <div className="sign-up-form">
          <div className="logo-and-sign-up-message">
            <img className="logo-sign-up-form" src="https://cdn-icons-png.flaticon.com/128/174/174849.png" alt="Logo" />
            <span>Log in</span>
          </div>

          <form onSubmit={handleLogin}>
            <div className="errors-for-sign-up">
              {errors.map((error, index) => (
                <div key={index}>{error}</div>
              ))}
            </div>
            <div className="all-sign-up-form-inputs-labels">
              <input
                className="sign-up-form-inputs-only"
                name="email"
                type="text"
                placeholder="Email"
                value={email}
                onChange={handleEmailChange}
              />
            </div>
            <div className="all-sign-up-form-inputs-labels">
              <input
                className="sign-up-form-inputs-only"
                name="password"
                type="password"
                placeholder="Password"
                value={password}
                onChange={handlePasswordChange}
              />
            </div>
            <div className="sign-up-submit-button-div">
              <button className="login-submit-button" type="submit">Sign in</button>
              <button className="login-submit-button" onClick={handleDemoUser}>Demo User</button>
            </div>
            <div className="terms-of-service-sign-up-div">
              <Link style={{ textDecoration: 'none', color: 'rgb(0,130,199)', fontSize: '.85em', cursor: 'not-allowed' }}></Link>
            </div>
            <div className="sign-up-form-gray-line-before-already-member" />
            <div className="already-a-member-sign-up">
              Not a member? <Link to="/sign-up" style={{ textDecoration: 'none', color: 'rgb(0,130,199)' }}>Sign up here.</Link>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default LoginForm;
