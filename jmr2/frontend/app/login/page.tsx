import Link from 'next/link'


export default function ChooseLogin() {
  return (
    <div>
      <p><Link href="/login/company">Company User</Link></p>
      <p><Link href="/login/jobseeker">Job Seeker</Link></p>
    </div>
  )
}
