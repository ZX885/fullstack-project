import './style.scss'
import { LogOutEntirely } from '../../conf/common.js';
import { useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';

function Profile() {
    const navigate = useNavigate()
    function logout() {
        navigate('../auth')
        LogOutEntirely()
        toast.success('Logged out successfuly', { toastId: 1})
    }

    return(
        <div id="profile-component">
            <h1>Profile</h1>

            <hr />

            <button className='danger-btn' onClick={logout}>
                Logout
            </button>
        </div>
    )
}

export default Profile;