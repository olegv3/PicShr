import React from "react";
import { useDispatch } from "react-redux";
import { useHistory, useParams } from "react-router-dom";
import { logout } from "../../store/session";
import './LogoutConfirm.css'

const LogoutConfirm = () => {
    const { id } = useParams()
    const dispatch = useDispatch()
    const history = useHistory()

    const onLogout = async (e) => {
        e.preventDefault()
        await dispatch(logout());
        return history.push('/')

    };

    const cancelButton = async (e, id) => {
        e.preventDefault()
        history.push(`/photos`)
    }

    return (
        <>
            <div className='background-for-signup-and-login'>
                <div className="confirm-delete-container">
                    <div className="sign-up-form">
                        <form>
                            <div className="confirm-delete-message" >
                            </div>
                            <div className='delete-cancel-button-div'>
                                <button className='sign-up-submit-button' onClick={e => onLogout(e)}>Logout</button>
                                <button className='sign-up-submit-button' onClick={event => cancelButton(event, id)}>Cancel</button>
                            </div>

                        </form>
                    </div>
                </div>
            </div>
        </>
    )
}

export default LogoutConfirm