import Link from 'next/link'


export default function CompanyUserLogin() {
  return (
    <>
      <form action="" method="POST">
        <label for="companyid">Company ID</label>
        <input type="text" name="companyid" />
        <label for="usernameoremail">Username or Email</label>
        <input type="text"name="usernameoremail" />
        <label for="password">Password</label>
        <input type="password" name="password" />
        <input type="submit" />
      </form>
      <p>New User? Sign Up <Link href="/signup">here</Link></p>
    </>
  )
}
