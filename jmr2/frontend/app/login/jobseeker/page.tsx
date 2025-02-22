import Link from 'next/link'


export default function JobSeekerLogin() {
  return (
    <>
      <form action="" method="POST">
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
