import { Outlet, Link } from 'react-router-dom'
import styles from './style.scss'
import emailVector from '../../assets/icons/email-vector.png'
import phoneVector from '../../assets/icons/phone-vector.png'

export default function Navigation() {
    return (
        <div className='main-navbar' style={styles}>
            <nav className='main-navbar '>
                <div className='upper-nav'>
                    <div className='left-nav'>
                        <a href="#">
                            <img src="mailto:zokirovzarruh@gmail.com" width="10" height="10" alt="" />
                            zokirovzarruh@gmail.com
                        </a>
                        <span>
                            <img src={phoneVector} width="10" height='10' alt="" />
                            (+99899) 2609264
                        </span>
                    </div>
                    <div className="right-nav"></div>
                </div>
            </nav>
          <Outlet />
        </div>
    )
}
