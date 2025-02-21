import Link from 'next/link'


export default function SignUp() {
  return (
    <>
      <form action="" method="POST">
        <label for="username">Username</label>
        <input type="text" name="username" />
        <label for="email">Email</label>
        <input type="email" name="email" />
        <label for="password">Password</label>
        <input type="password" name="password" />
        <label for="passwordconfirmation">Re-type Password</label>
        <input type="password" name="passwordconfirmation" />
        <label for="company">Company</label>
        <input type="checkbox" name="company" />
        <input type="submit" />
      </form>
      <p>Already have an account? Log In <Link href="/login">here</Link></p>
    </>
  )
}
